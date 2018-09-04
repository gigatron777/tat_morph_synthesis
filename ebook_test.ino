#include <SPI.h>
#include <SD.h>
#include <LiquidCrystal.h>

LiquidCrystal lcd(7, 6, 5, 4, 3, 2);
const uint8_t PIN_CS = 10, BUTTON_UP = 8, BUTTON_DOWN = 9;
byte row_to_print = 0, btn_up_press_flag = 0, btn_down_press_flag = 0;
char buf[16];

unsigned long cur_file_pos = 0, cur_file_size, btn_up_last_press = 0, btn_down_last_press = 0;
File cur_file;


void lcd_println(char str[])
{
  if (row_to_print == 2)
  {
    lcd.clear();
    row_to_print = 0;
  }
  lcd.setCursor(0, row_to_print);
  lcd.print(str);
  row_to_print++;
}

byte file_read_block(File &file, char str[], unsigned long pos)//read 16 chars from file after given position
{
  //unsigned long file_size = file.size();
  unsigned long end_pos = min(pos + 16, file.size()), i = 0;
  if (pos > end_pos)
  {
    return 0;
  }
  file.seek(pos);
  do
  {
    str[i] = file.read();
    i++;
  } while (pos + i < end_pos);
  Serial.println("i = " + String(i - 1));
  return 1;
}


//----------------------------------------------------------
void setup() {
  Serial.begin(9600);
  lcd.begin(16, 2);

  pinMode(BUTTON_UP, INPUT);
  pinMode(BUTTON_DOWN, INPUT);

  if(!SD.begin(PIN_CS))
  {
    lcd_println("Error!");
    lcd_println("SDcard not found");
    return;
  }
  cur_file = SD.open("newton.txt", FILE_READ);
  cur_file_size = cur_file.size();
  if (cur_file)
  {
    file_read_block(cur_file, buf, cur_file_pos);
    lcd_println(buf);
    cur_file_pos += 16;
    file_read_block(cur_file, buf, cur_file_pos);
    lcd_println(buf);
    cur_file_pos += 16;
  }
  //cur_file.close();
}

void scrollUp()
{
  if (cur_file_pos > 0)
  {
    cur_file_pos -= 64;
    file_read_block(cur_file, buf, cur_file_pos);
    lcd_println(buf);
    cur_file_pos += 16;
    
    file_read_block(cur_file, buf, cur_file_pos);
    lcd_println(buf);
    cur_file_pos += 16;
  }
}

void scrollDown()
{
  //Serial.println("file pos:" + String(cur_file_pos));
  if (cur_file_pos + 31 < cur_file_size)
  {
    file_read_block(cur_file, buf, cur_file_pos);
    lcd_println(buf);
    cur_file_pos += 16;

    file_read_block(cur_file, buf, cur_file_pos);
    lcd_println(buf);
    cur_file_pos += 16;
  }
}

void loop() {
  
  if (digitalRead(BUTTON_UP) == HIGH && btn_up_press_flag == 0 && millis() - btn_up_last_press > 150)
  {
    scrollUp();
    btn_up_last_press = millis();
    btn_up_press_flag = 1;
  }
  if (digitalRead(BUTTON_UP) == LOW && btn_up_press_flag == 1)
  {
    btn_up_press_flag = 0;
    btn_up_last_press = millis();
  }
 //-------------------------
  if (digitalRead(BUTTON_DOWN) == HIGH && btn_down_press_flag == 0 && millis() - btn_down_last_press > 150)
  {
    scrollDown();
    btn_down_last_press = millis();
    btn_down_press_flag = 1;
  }
  if (digitalRead(BUTTON_DOWN) == LOW && btn_down_press_flag == 1)
  {
    btn_down_press_flag = 0;
    btn_down_last_press = millis();
  }
  

}
