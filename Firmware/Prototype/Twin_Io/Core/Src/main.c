/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.c
  * @brief          : Main program body
  ******************************************************************************
  * @attention
  *
  * Copyright (c) 2024 STMicroelectronics.
  * All rights reserved.
  *
  * This software is licensed under terms that can be found in the LICENSE file
  * in the root directory of this software component.
  * If no LICENSE file comes with this software, it is provided AS-IS.
  *
  ******************************************************************************
  */
/* USER CODE END Header */
/* Includes ------------------------------------------------------------------*/
#include "main.h"
#include "dma.h"
#include "spi.h"
#include "tim.h"
#include "usart.h"
#include "gpio.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */

/* USER CODE END Includes */

/* Private typedef -----------------------------------------------------------*/
/* USER CODE BEGIN PTD */

/* USER CODE END PTD */

/* Private define ------------------------------------------------------------*/
/* USER CODE BEGIN PD */
#define ADC_CMD_NULL	0x0000
#define ADC_CMD_RESET   0x0011
#define ADC_CMD_STANDBY 0x0022
#define ADC_CMD_WAKEUP  0x0033
#define ADC_CMD_LOCK	0x0555
#define ADC_CMD_UNLOCK	0x0655

#define RREG	0x20
#define WREG	0x40
/* USER CODE END PD */

/* Private macro -------------------------------------------------------------*/
/* USER CODE BEGIN PM */

/* USER CODE END PM */

/* Private variables ---------------------------------------------------------*/

/* USER CODE BEGIN PV */
uint8_t pu8_Adc0Rdy[3];
/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
/* USER CODE BEGIN PFP */
uint32_t u32_AdcTransmitReceive (SPI_HandleTypeDef *hspi, uint32_t u32_Data);
void v_SelectAdc(uint8_t u8_AdcNum, uint8_t on);

uint8_t u8_ADCReadReg(uint8_t u8_AdcNum, uint8_t u8_RegAddr);
uint8_t u8_ADCWriteReg(uint8_t u8_AdcNum, uint8_t u8_RegAddr, uint8_t u8_Val);
uint8_t u8_ADCCommand(uint8_t u8_AdcNum, uint16_t u16_Command);
uint8_t u8_AllADCCommand(uint16_t u16_Command);
uint8_t u8_AllADCWriteReg(uint8_t u8_RegAddr, uint8_t u8_Val);

/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */

/* USER CODE END 0 */

/**
  * @brief  The application entry point.
  * @retval int
  */
int main(void)
{
  /* USER CODE BEGIN 1 */

  /* USER CODE END 1 */

  /* MCU Configuration--------------------------------------------------------*/

  /* Reset of all peripherals, Initializes the Flash interface and the Systick. */
  HAL_Init();

  /* USER CODE BEGIN Init */

  /* USER CODE END Init */

  /* Configure the system clock */
  SystemClock_Config();

  /* USER CODE BEGIN SysInit */

  /* USER CODE END SysInit */

  /* Initialize all configured peripherals */
  MX_GPIO_Init();
  MX_DMA_Init();
  MX_SPI1_Init();
  MX_USART3_UART_Init();
  MX_TIM2_Init();
  MX_USART1_UART_Init();
  /* USER CODE BEGIN 2 */
  HAL_UART_MspInit(&huart1);

  HAL_TIM_PWM_Start(&htim2, TIM_CHANNEL_2);	//Start the ADC clock generation

  //Init all ADCs
  HAL_Delay(100);
  u8_AllADCCommand(ADC_CMD_RESET);	//Reset the ADC to POR
  HAL_Delay(100);
  u8_AllADCCommand(ADC_CMD_NULL);	//Wake up the SPI interface (See datasheet P37)
  HAL_Delay(100);
  u8_AllADCCommand(ADC_CMD_UNLOCK);	//Unlock the ADC registers so they can be written to
  HAL_Delay(100);
  u8_AllADCWriteReg(0xF, 0xF);		//Enable all ADC Channels
  HAL_Delay(100);
  //u8_AllADCWriteReg(0xD, 0b00000100);		//Set fIclk = fclk/4
  HAL_Delay(100);
  u8_AllADCWriteReg(0xE, 0b00100101);		//Set fMod = fIclk/2 and fdata=fmod/512
  HAL_Delay(100);
  u8_AllADCWriteReg(0x11, 0b00000000); //Select gain 2x for channel 0
  HAL_Delay(100);
  u8_AllADCWriteReg(0x12, 0b00000000); //Select gain 2x for channel 1
  HAL_Delay(100);
  u8_AllADCWriteReg(0x13, 0b00000000); //Select gain 2x for channel 2
  HAL_Delay(100);
  u8_AllADCWriteReg(0x14, 0b00000000); //Select gain 2x for channel 3
  HAL_Delay(100);
  u8_AllADCWriteReg(0xB, 0b01101000);
  HAL_Delay(100);
	u8_AllADCWriteReg(0xC, 0b00111100);
  HAL_Delay(100);
  u8_AllADCCommand(ADC_CMD_WAKEUP);	//Wake the ADC up and start measuring
  HAL_Delay(100);
  u8_AllADCCommand(ADC_CMD_LOCK);	//Lock the ADC registers so they cant be written to




  /* USER CODE END 2 */

  /* Infinite loop */
  /* USER CODE BEGIN WHILE */
  while (1)
  {

	  for(uint8_t i = 0; i <= 2; i++)
	  {
		  if(pu8_Adc0Rdy[i])
		  {
			  v_SelectAdc(i, 1); // Select the ADC

			  pu8_Adc0Rdy[i] = 0; //Reset the Flag

			  uint8_t pu8_UartBuf[14];
			  uint8_t u8_UartBufCnt=0;			//init the counter which keeps track of the number of bits to be sent

			  pu8_UartBuf[u8_UartBufCnt] = i;	//Transmit the current ADC number which the samples are from
			  u8_UartBufCnt++;

			  for(uint8_t j=0;j<15;j++)//output bytes 3-14 because 0-2 are status bytes
			  {
				  while (((SPI1->SR)&(1<<7))) {};  // wait for BSY bit to Reset -> This will indicate that SPI is not busy in communication
				  SPI1->DR = 0;	//send a dummy byte to receive next byte
				  while (!((SPI1->SR) &SPI_SR_RXNE)){};  // Wait for RXNE to set -> This will indicate that the Rx buffer is not empty

				  if(j>=3)
				  {
					 pu8_UartBuf[u8_UartBufCnt] = SPI1->DR;	//Transmit the current ADC number which the samples are from
					 u8_UartBufCnt++;
				  }
				  else
				  {
					  SPI1->DR; //Discard the SPI data
				  }
			  }
			  while (((SPI1->SR)&(1<<7))) {};  // wait for BSY bit to Reset -> This will indicate that SPI is not busy in communication
			  pu8_UartBuf[u8_UartBufCnt] = '\n';	//Transmit the current ADC number which the samples are from
			  u8_UartBufCnt++;
			  HAL_StatusTypeDef err;
			  while(huart1.gState != HAL_UART_STATE_READY);
			  err = HAL_UART_Transmit_DMA(&huart1, pu8_UartBuf, u8_UartBufCnt);
			  if(err!=HAL_OK)
			  {
				  __NOP();
			  }

			  __HAL_UART_DISABLE_IT(&huart1, UART_IT_TXE);
			  v_SelectAdc(i, 0); //Deselect the ADC

		  }
	  }

    /* USER CODE END WHILE */

    /* USER CODE BEGIN 3 */
  }
  /* USER CODE END 3 */
}

/**
  * @brief System Clock Configuration
  * @retval None
  */
void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};

  /** Initializes the RCC Oscillators according to the specified parameters
  * in the RCC_OscInitTypeDef structure.
  */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSE;
  RCC_OscInitStruct.HSEState = RCC_HSE_ON;
  RCC_OscInitStruct.HSEPredivValue = RCC_HSE_PREDIV_DIV2;
  RCC_OscInitStruct.HSIState = RCC_HSI_ON;
  RCC_OscInitStruct.Prediv1Source = RCC_PREDIV1_SOURCE_HSE;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
  RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSE;
  RCC_OscInitStruct.PLL.PLLMUL = RCC_PLL_MUL8;
  RCC_OscInitStruct.PLL2.PLL2State = RCC_PLL_NONE;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    Error_Handler();
  }

  /** Initializes the CPU, AHB and APB buses clocks
  */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV2;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_2) != HAL_OK)
  {
    Error_Handler();
  }

  /** Configure the Systick interrupt time
  */
  __HAL_RCC_PLLI2S_ENABLE();
}

/* USER CODE BEGIN 4 */
uint32_t u32_AdcTransmitReceive (SPI_HandleTypeDef *hspi, uint32_t u32_Data)
{
	uint8_t pu8_TxData[3];
	uint8_t pu8_RxData[3];
	for(int i = 2; i > 0; i--)
	{
		pu8_TxData[i] = (u32_Data & 0xFF << (8*i)) >> (8*i);
		/*
		 * pu8_Data[0] = MSB
		 * pu8_Data[2] = LSB
		 */
	}
	HAL_SPI_TransmitReceive(&hspi1, pu8_TxData, pu8_RxData, 3, 100);
	return pu8_RxData[0] | pu8_RxData[1] << 8 | pu8_RxData[2] << 16;
}

void v_SelectAdc(uint8_t u8_AdcNum, uint8_t on)
{
	switch (u8_AdcNum)
	{
	case 0:
		HAL_GPIO_WritePin(ADC0_CS_GPIO_Port, ADC0_CS_Pin, !on);
		break;
	case 1:
		HAL_GPIO_WritePin(ADC1_CS_GPIO_Port, ADC1_CS_Pin, !on);
		break;
	case 2:
		HAL_GPIO_WritePin(ADC2_CS_GPIO_Port, ADC2_CS_Pin, !on);
		break;
	default:
		break;
	}
}

void HAL_GPIO_EXTI_Callback(uint16_t GPIO_Pin)
{
  if(GPIO_Pin == ADC0_DRDY_Pin) {
    pu8_Adc0Rdy[0] = 1;
  }
  else
  if(GPIO_Pin == ADC1_DRDY_Pin) {
	pu8_Adc0Rdy[1] = 1;
  }
  else
  if(GPIO_Pin == ADC2_DRDY_Pin) {
	pu8_Adc0Rdy[2] = 1;
  }
}

uint8_t u8_ADCReadReg(uint8_t u8_AdcNum, uint8_t u8_RegAddr)
{

	//uint8_t u8_Val = 0;
	u8_RegAddr |= RREG;
	u8_ADCCommand(u8_AdcNum, u8_RegAddr << 8);

	v_SelectAdc(u8_AdcNum, 1);

	uint8_t pu8_RecvBuf[3];
	uint8_t pu8_ZeroBuf[3] = {0,0,0};
	HAL_SPI_TransmitReceive(&hspi1, pu8_ZeroBuf, pu8_RecvBuf, 3, 100);
	v_SelectAdc(u8_AdcNum, 0);
	return pu8_RecvBuf[1];

}

uint8_t u8_ADCWriteReg(uint8_t u8_AdcNum, uint8_t u8_RegAddr, uint8_t u8_Val)
{
	u8_RegAddr |= WREG;

	u8_ADCCommand(u8_AdcNum, u8_RegAddr << 8 | u8_Val);
	/*
	v_SelectAdc(u8_AdcNum, 1);
	HAL_SPI_Transmit(&hspi1, &u8_RegAddr, 1, 100);

	HAL_SPI_Transmit(&hspi1, &u8_Val, 1, 100);
	v_SelectAdc(u8_AdcNum, 0);*/
	return 0;
}

uint8_t u8_AllADCWriteReg(uint8_t u8_RegAddr, uint8_t u8_Val)
{
	for(uint8_t i = 0; i < 3; i++)
	{
		u8_ADCWriteReg(i, u8_RegAddr, u8_Val);
		HAL_Delay(10);
	}
	return 0;
}

uint8_t u8_ADCCommand(uint8_t u8_AdcNum, uint16_t u16_Command)
{
	uint8_t u8_MSB = u16_Command >> 8;
	uint8_t u8_LSB = u16_Command & 0xFF;
	v_SelectAdc(u8_AdcNum, 1);
	HAL_SPI_Transmit(&hspi1, &u8_MSB, 1, 100);
	HAL_SPI_Transmit(&hspi1, &u8_LSB, 1, 100);
	uint8_t u8_Zero = 0;
	HAL_SPI_Transmit(&hspi1, &u8_Zero, 1, 100);
	v_SelectAdc(u8_AdcNum, 0);
	return 0;
}

uint8_t u8_AllADCCommand(uint16_t u16_Command)
{
	for(uint8_t i = 0; i < 3; i++)
	{
		u8_ADCCommand(i, u16_Command);
		HAL_Delay(10);
		u8_ADCCommand(i, ADC_CMD_NULL);//Send a NULL command to read back the data
	}
	return 0;
}

/* USER CODE END 4 */

/**
  * @brief  This function is executed in case of error occurrence.
  * @retval None
  */
void Error_Handler(void)
{
  /* USER CODE BEGIN Error_Handler_Debug */
  /* User can add his own implementation to report the HAL error return state */
  __disable_irq();
  while (1)
  {
  }
  /* USER CODE END Error_Handler_Debug */
}

#ifdef  USE_FULL_ASSERT
/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t *file, uint32_t line)
{
  /* USER CODE BEGIN 6 */
  /* User can add his own implementation to report the file name and line number,
     ex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
  /* USER CODE END 6 */
}
#endif /* USE_FULL_ASSERT */
