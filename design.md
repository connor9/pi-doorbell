# Design

One raspberry pi doorbell should allow you to configure
multiple virtual devices so that they can
be configured to play different tones and have different
API endpoints.

Considerations:
* Should devices allow internal linking / grouping?

## Actions

Potential actions from existing doorbell designs

Switch On Action: 
*  Determines what happens when the switch.on command is executed.
 (Do Nothing,
  Play Default Chime, 
 Turn On LED, Turn On Siren, Turn On Strobe, Turn On Siren/Strobe,
  Play Tone #1 - Play Tone #30)
* Siren Sound: (Tone #1 - Tone #30)
* Siren Volume: (Mute, 1% - 100%)
* Strobe Light Effect: (Off, On, Slow Pulse, Pulse, Fast Pulse, Flash, Strobe)
* Siren Repeat: (Unlimited, 1 - 250)
* Siren Repeat Delay: (No Delay, 1 Second - 250 Seconds)
* Siren Intercept Length: (Play Entire Tone, 1 Second - 250 Seconds)
* Default Chime Sound: (Tone #1 - Tone #30)
* Default Chime Volume: (Mute, 1% - 100%)
* Chime Light Effect: (Off, On, Slow Pulse, Pulse, Fast Pulse, Flash, Strobe)
* Chime Repeat: (1 - 255)
* Chime Repeat Delay: (No Delay, 1 Second - 250 Seconds)
* Chime Intercept Length: (Play Entire Tone, 1 Second - 250 Seconds)

## API

The aim is to make it similar to the HUE / Deconz API
endpoints for familiarity.

```
API/devices
{
    "12345guid" : {
        "name": "Front Door",
        "type": "Warning device",
        "state": {
            "alert": "strobe",
            "reachable": true,
            "lastupdated": "2018-02-27T19:42:19"
        },
        "config": {
            "maxduration": 300,
            "on_action": "chime+strobe"
        }
    }
}
```