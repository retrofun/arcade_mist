Scripts and database to create a markdown table of available Arcade cores for [MiST](https://github.com/mist-devel/mist-board/wiki) FPGA

* `mist_fpga_cores_arcade_mist.sh`: Helper bash script that parses [Gehstock's Arcades](https://github.com/Gehstock/Mist_FPGA_Cores/tree/master/Arcade_MiST) from the README.txt file and outputs them as CSV.
* `jotego_arcades.sh`: Helper bash script that parses [Jotego's Arcades](https://github.com/jotego/jtbin) mra files for the available cores.
* `arcade_mist.py`: Python 3 script that parses `arcade_mist.sqlite` and outputs a markdown table of available Arcade cores. Result is used on the [CoreStatus](https://github.com/mist-devel/mist-board/wiki/CoreStatus#arcade) page of the [MiST wiki](https://github.com/mist-devel/mist-board/wiki).
* `arcade_mist.sqlite`: Arcade MiST SQLite database.
