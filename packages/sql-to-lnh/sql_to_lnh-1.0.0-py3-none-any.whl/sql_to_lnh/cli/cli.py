from sql_to_lnh.CodeGenerator import CodeGenerator

with CodeGenerator('sql_to_lnh.db') as t:
	continue_flag = True
	while continue_flag:
		try:
			print('Введите SQL-выражение')
			cur = input('>>> ')
			sql_stmt = cur
			while cur != '':
				cur = input('>>> ')
				sql_stmt += f'\n{cur}'
			print('Имя объекта (Enter для имени по-умолчанию): ')
			ref_name = input()
			if ref_name == '':
				ref_name = None
			print('Результат трансляции:')
			res = t.translate(sql_stmt, ref_name)
			for code in res:
				print(code)
		except KeyboardInterrupt:
			continue_flag = False
		except Exception as e:
			print(f'Ошибка: {e}')
