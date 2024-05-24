# All-Russian Classifier of Municipal Territories (OKTMO) Parser #

## What is this? ##
Simple and useful parser that helps you get actual All-Russian Classifier of Municipal Territories (OKTMO).

## Quick Guide ##
The parser is based on the following structure:

    parser = OktmoParser()
    start_keyword = ''
    end_keyword = ''
    parser.parse_oktmo(start_keyword, end_keyword)
    
Parser returns .json file with actual OKTMO from [Federal State Statistics Service](https://rosstat.gov.ru/).


----------


### Using ###


Using the library is as simple and convenient as possible:

1. Import:

`from OktmoParser import OktmoParser`

2. Create object:

`parser = OktmoParser()`

3. Set `start_keyword` value and `end_keyword` value.

*Notice:* for the first usage set it empty to get full .json file to see the structure and then you can set your values.

Examples:

    start_keyword = 'Муниципальные образования Приморского края'
    end_keyword = 'Муниципальные образования Ставропольского края'

You will get all rows between this municipal territories.

4. Parse and get .json file:

`parser.parse_oktmo(start_keyword, end_keyword)`

5. That's it.


----------


## Developer ##
[@letimvkocmoc](https://github.com/letimvkocmoc/) 