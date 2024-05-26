==========================
Plover Vipe
==========================

Vipe (Norwegian stenography system) support for Plover.

It remaps W to V and Z to N. I have also added some simple ortography rules.


The steno keyboard chart. 
--------------------------

This chart contains the letters for norwegian steno
https://docs.google.com/drawings/d/1m3cIkRPlEk2SmmVI_mmRBNIiuxUh-wDy2_A_Pn_ZUZQ/edit?usp=sharing


this chart contains most of the letter combinations
https://docs.google.com/drawings/d/1TlvdrWSf1BHJG6P3KkEr4j49XLYwzMm85dw4BtpkfPo/edit?usp=sharing



Recommended Usage
-----------------

Since the Vipe dictionary will change in the future, it it highly recommended to create a separate dictionary with your own mappings.


Installation
------------

To install the cloned git repository, you can run the following command:

Windows

.. code:: powershell

	.\plover_console.exe -s plover_plugins install git+https://github.com/nikolasnjerve/Plover__Vipe

Mac

.. code:: bash

	/Applications/Plover.app/Contents/MacOS/Plover -s plover_plugins install https://github.com/nikolasnjerve/Plover__Vipe


Special Thanks
--------------

Special thanks to Martin Koerner for letting me use Regenpfeifer as a template for Vipe.

License
-------

This plugin is licensed under GPLv3, or any later version.

