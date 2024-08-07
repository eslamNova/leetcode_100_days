#include <millisDelay.h>
#include <EEPROM.h>
#include "DFRobotDFPlayerMini.h" // MUSIC

char Incoming_value = 0;
unsigned long MAIN_TIME = 0;
const unsigned long FREEZE_TIME = 10000;
const unsigned long MUSIC_TIME = 12000;
static unsigned long lastRefreshTime = 0;

int led = 13;

int sw1 = 8;
int sw2 = 9;
int sw3 = 10;
int sw4 = 11;

int enableButton = 2;  // Button to enable the timer
int disableButton = 3; // Button to disable the timer

int t, m, s;

char command;
bool debug = false;

millisDelay mainDelay;
millisDelay freezeDelay;
millisDelay musicDelay;
DFRobotDFPlayerMini myDFPlayer; // MUSIC

unsigned long mainRemainingTime = 0;
unsigned long currentMillis = 0;
unsigned long cumulativeTime = 0;

void setup()
{
    pinMode(led, OUTPUT);
    pinMode(sw1, OUTPUT);
    pinMode(sw2, OUTPUT);
    pinMode(sw3, OUTPUT);
    pinMode(sw4, OUTPUT);

    pinMode(enableButton, INPUT_PULLUP);  // Configure the enable button
    pinMode(disableButton, INPUT_PULLUP); // Configure the disable button

    digitalWrite(led, LOW);
    digitalWrite(sw1, LOW);
    digitalWrite(sw2, LOW);
    digitalWrite(sw3, LOW);
    digitalWrite(sw4, LOW);

    if (debug)
        Serial.begin(9600); // Built-in Serial for debugging

    Serial1.begin(9600); // Bluetooth Serial
    if (debug)
        Serial.println("Bluetooth IVDT Control - Ready");

    Serial3.begin(9600); // MP3 Player Serial
    if (debug)
        Serial.println("Starting MP3 Player initialization...");

    if (!myDFPlayer.begin(Serial3))
    {
        if (debug)
            Serial.println("Unable to begin: Please check the connection and try again.");
        while (true)
            ;
    }
    if (debug)
        Serial.println("DFPlayer Mini online.");

    myDFPlayer.setTimeOut(500); // Timeout serial 500ms
    myDFPlayer.volume(30);      // Volume 30
    myDFPlayer.EQ(0);
    if (debug)
        Serial.println("MP3 Player settings configured.");

    command = '3' - 48;
    myDFPlayer.play(command);
    if (debug)
        Serial.println("MP3 Player setup complete, playing initial track.");

    EEPROM.get(0, cumulativeTime);

    if (debug)
    {
        Serial.print("Cumulative Time from EEPROM: ");
        Serial.println(cumulativeTime);
    }

    if (debug)
        Serial.println("Setup complete");
}

void loop()
{
    delay(100);

    if (Serial1.available() > 0)
    {
        Incoming_value = Serial1.read();
        if (debug)
        {
            Serial.print("Incoming value: ");
            Serial.println(Incoming_value);
        }

        switch (Incoming_value)
        {
        case '1':
            MAIN_TIME = 10000;
            command = '2' - 48;
            myDFPlayer.play(command);
            musicDelay.start(MUSIC_TIME);
            if (debug)
                Serial.println("Case 1: Play command 2, MAIN_TIME set to 5000");
            cumulativeTime += 10; // Add to cumulative time
            EEPROM.put(0, cumulativeTime);
            break;
        case '2':
            MAIN_TIME = 20000;
            command = '2' - 48;
            myDFPlayer.play(command);
            musicDelay.start(MUSIC_TIME);
            if (debug)
                Serial.println("Case 2: Play command 2, MAIN_TIME set to 10000");
            cumulativeTime += 20; // Add to cumulative time
            EEPROM.put(0, cumulativeTime);
            break;
        case '3':
            MAIN_TIME = 30000;
            command = '2' - 48;
            myDFPlayer.play(command);
            musicDelay.start(MUSIC_TIME);
            if (debug)
                Serial.println("Case 3: Play command 2, MAIN_TIME set to 15000");
            cumulativeTime += 30; // Add to cumulative time
            EEPROM.put(0, cumulativeTime);
            break;
        case '9':
            mainRemainingTime = mainDelay.remaining();
            mainDelay.stop();
            freezeDelay.start(FREEZE_TIME);
            if (debug)
            {
                Serial.print("Case 9: Freeze for 10 seconds, mainRemainingTime: ");
                Serial.println(mainRemainingTime);
            }
            break;
        case '7':
            MAIN_TIME = 0;
            mainDelay.stop();
            musicDelay.stop();
            myDFPlayer.stop();
            if (debug)
                Serial.println("Case 7: Stop all delays and player");
            break;
        case '5': // Send cumulative time over Bluetooth
            // Serial1.print("Cumulative Time: ");
            Serial1.println(cumulativeTime);
            if (debug)
            {
                Serial.print("Sent cumulative time: ");
                Serial.println(cumulativeTime);
            }
            break;

        default:
            if (debug)
                Serial.println("Unknown command received");
            break;
        }
    }

    if (digitalRead(enableButton) == LOW)
    { // Check if the enable button is pressed
        MAIN_TIME = 15000;
        command = '2' - 48;
        myDFPlayer.play(command);
        musicDelay.start(MUSIC_TIME);

        if (debug)
            Serial.println("Enable button pressed, MAIN_TIME set to 15000");
        cumulativeTime += 15; // Add to cumulative time
        EEPROM.put(0, cumulativeTime);
    }

    if (digitalRead(disableButton) == LOW)
    { // Check if the disable button is pressed
        MAIN_TIME = 0;
        mainDelay.stop();
        musicDelay.stop();
        myDFPlayer.stop();

        if (debug)
            Serial.println("Disable button pressed, all delays and player stopped");
    }

    if (mainDelay.isRunning())
    {
        digitalWrite(led, HIGH); // LED on while main delay is running
        digitalWrite(sw1, HIGH);
        digitalWrite(sw2, HIGH);
        digitalWrite(sw3, HIGH);
        digitalWrite(sw4, HIGH);
        if (millis() - lastRefreshTime >= 1000)
        {
            lastRefreshTime = millis();
            t = mainDelay.remaining() / 1000;
            m = t / 60;
            s = t % 60;
            Serial1.println(t);
            if (debug)
            {
                Serial.print("Main delay running, remaining time: ");
                Serial.println(t);
            }
        }
    }
    else
    {
        digitalWrite(led, LOW); // LED off otherwise
        digitalWrite(sw1, LOW);
        digitalWrite(sw2, LOW);
        digitalWrite(sw3, LOW);
        digitalWrite(sw4, LOW);
        // if (debug) Serial.println("Main delay not running, LED off");
    }

    if (mainDelay.justFinished())
    {
        digitalWrite(led, LOW); // turn the LED off
        digitalWrite(sw1, LOW);
        digitalWrite(sw2, LOW);
        digitalWrite(sw3, LOW);
        digitalWrite(sw4, LOW);

        delay(2000);
        Serial1.println(0);
        if (debug)
            Serial.println("Main delay just finished, LED off");
    }

    if (freezeDelay.justFinished())
    {
        if (mainRemainingTime > 0)
        {
            mainDelay.start(mainRemainingTime);
            if (debug)
                Serial.println("Freeze delay just finished, resuming main delay");
        }
    }

    if (musicDelay.justFinished())
    {
        if (MAIN_TIME > 0)
        {
            mainDelay.start(MAIN_TIME);
            if (debug)
                Serial.println("Music delay just finished, starting main delay");
        }
    }
}
