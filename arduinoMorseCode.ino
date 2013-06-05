int led = 7;

void setup()
{
  Serial.begin(9600);
  pinMode(led,OUTPUT);
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
    
    //Asking if ready
    else if(c=='r')
    {
      Serial.write('1');
    }
  }
}
