from datetime import datetime

time = datetime.now().strftime('%Y%m%d%H%M%S')

print('# set TIMESTAMP', time)
print(f'##vso[task.setvariable variable=TIMESTAMP]{time}')
