/*	----------------------------------------------------------------------------
	interrupt library demo
	----------------------------------------------------------------------------
	author:			Régis Blanchot
	first release:	19/12/2010
	last update:	24/12/2010
	pinguino ide:	9.5
 	boards:			8-bit ONLY
	wiring:			leds on pin 0 to 3 (RB0 to RB3)
					ex.: RB0 --- 470 Ohms ---<|--- GND
	--------------------------------------------------------------------------*/

#define LED0	0
#define LED1	1
#define LED2	2
#define LED3	3

void blink0() {	toggle(LED0); }
void blink1() {	toggle(LED1); }
void blink2() {	toggle(LED2); }
void blink3() {	toggle(LED3); }

void setup()
{
	// Clear RB3 to RB0
	LATB  &= 0b11110000;
	PORTB &= 0b11110000;
	// RB3 to RB0 are OUTPUT
	TRISB &= 0b11110000;

	OnTimer0(blink0, INT_MILLISEC, 500);	// Use Timer0 to toggle pin 0 every 500 ms
	OnTimer1(blink1, INT_MILLISEC, 500);	// Use Timer1 to toggle pin 0 every 500 ms
	OnTimer2(blink2, INT_MILLISEC, 500);	// Use Timer2 to toggle pin 0 every 500 ms
	OnTimer3(blink3, INT_MILLISEC, 500);	// Use Timer3 to toggle pin 0 every 500 ms
}

void loop()
{
}