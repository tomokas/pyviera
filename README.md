# PyViera

## What?
PyViera allows you control your Panasonic VIERA TV programmatically.

## Which TVs are compatible?
Taken directly from the 'Compatible VIERA models section' from the description of the Viera remote app on the App Store:

    <<2011 Models (Series)>>
    North America: VT30, GT30, ST30, PST34, GT31, DT30, D30
    Latin America: VT30, GT30, ST30, DT30, E30
    Europe/CIS: VT30, GT30, GW30, GTX34, GTN33, GTF32, GTS31, G30, ST30, ST31, ST33, S30, S31, UT30, DT35, DT30, D35, D30, E30, E31, EX34, EN33, EF32, ES31, EW30
    Australia/New Zealand: VT30, GT30, ST30, DT30, E30
    Malaysia/Thai Land/Singapore/Indonesia/Middle East/Iran: VT30, ST30, DT30, E30
    Vietnam/Philippines: VT30, ST30, DT30
    India: VT30, ST30, E30
    Saudi Arabia: VT30, ST30, UT30
    South Africa: VT30, UT30
    China: VT30, VT31, GT30, GT31, GT32, ST30, ST32, S30, DT30
    Hong Kong: ST30
    Taiwan: VT30, ST30, E30
    Japan: VT3, GT3, ST3, DT3
    (As of July 22, 2011)

## How?
In a nutshell:

```python
    from pyviera import VieraFinder
    vf = VieraFinder()
    tv = vf.get_viera()
    tv.num(18)
    tv.mute()
    tv.mute() # Toggles
    tv.vol_up()
```

Check out the `Viera` class in `viera.py` for all the supported keys. They're all pretty self-explanatory.

## Contributors
Many thanks to:
 - [Tenderfoot14](https://github.com/Tenderfoot14) for adding lots of new SOAP codes.
