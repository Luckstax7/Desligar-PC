import os
import datetime

agora = datetime.datetime.now()


def relogio(hora_marcada):
	tempo = datetime.datetime.strptime(x, '%H:%M').replace(year=agora.year, month=agora.month, day=agora.day)
	if tempo < agora:
		tempo = tempo + datetime.timedelta(days=1)
	escolha = str(input('Digite S para desligar e R para reiniciar:'))

	hora_marcada = (tempo - agora).seconds
	os.system(f'shutdown /{escolha} /t {hora_marcada}')


def cronometro(hora_marcada):
	tempo = datetime.datetime.strptime(x, '%H:%M').replace(year=agora.year, month=agora.month, day=agora.day)
	if tempo < agora:
		tempo = tempo + datetime.timedelta(days=1)
	escolha = str(input('Digite S para desligar e R para reiniciar:'))
	hora_marcada = (tempo - agora).seconds
	os.system(f'shutdown /{escolha} /t {hora_marcada}')


opcao = str(input('Digite 1 para definir horario\n 2 para contagem regressiva\n 3 para cancelar o desligamento:'))
if opcao == '1':
	x = str(input('Digite que hora quer que desligue:'))
	relogio(x)
elif opcao == '2':
	x = str(input('Digite quanto tempo até desligar:'))
	cronometro(x)
elif opcao == '3':
	os.system(f'shutdown /a')
else:
	print('opção invalida, presta atenção')

