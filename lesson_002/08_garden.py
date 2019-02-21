#!/usr/bin/env python
# -*- coding: utf-8 -*-

garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

garden_set = set(garden)

meadow_set = set(meadow)

# выведите на консоль все виды цветов
land = garden_set | meadow_set
print('все виды цветов:', land)

# выведите на консоль те, которые растут и там и там
land2 = garden_set & meadow_set
print('виды цветов которые растут в саду и на лугу:', land2)

# выведите на консоль те, которые растут в саду, но не растут на лугу
land3 = garden_set - meadow_set
print('цветы которые растут в саду, но не растут на лугу:', land3)

# выведите на консоль те, которые растут на лугу, но не растут в саду
land4 = meadow_set - garden_set
print('цветы которые растут на лугу, но не растут в саду:', land4)


