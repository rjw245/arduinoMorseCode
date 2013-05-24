int led = 7;

void setup()
{
  Serial.begin(9600);
  pinMode(led,OUTPUT);
  //Send ready signal
  Serial.write('1');
}

void loop()
{
  if(Serial.available()){
    char c = Serial.read();
    if(c=='1')
    {
      digitalWrite(led,HIGH);
    }
    else if(c=='0')
    {
      digitalWrite(led,LOW);
    }
  }
}
