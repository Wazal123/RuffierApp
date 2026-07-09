
from PyQt5.QtCore import QTime


win_x, win_y = 100, 100
win_width, win_height = 1000, 600


txt_hello = '¡Bienvenido al Programa de detección de estado de salud!'
txt_next = 'Iniciar'
txt_instruction = ('Esta aplicacion le permite usar la prueba de Ruffier para realizar un diagnostico inicial de su salud.\n'
                   'La prueba de Ruffier es un conjunto de ejercicios fisicos diseñado para evaluar su rendimiento cardiaco udurante el esfuerzo fisico.\n'
                   'El sujeto se tumba en posicion supina durante 5 minutos y se toma la frecuencia del pulso durante 15 segundos;\n'
                   'y luego durante los ultimos 15 segundos del primer minutos de recuperacion. \n'
                   '¡Importante el Si no se siente bien durante la prueba (mareos, \n'
                   'tinnitus, falta de respiracion, etc.), detenga la prueba y consulte a un medico.' )
txt_title = 'Salud'
txt_name = 'Introduzca su nombre completo:'
txt_hintname = '0'
txt_test1 = 'Acuestese y tome su pulso durante 15 segundos. Haga clic en el boton "Iniciar primera prueba" para iniciar el temporizador. \nEscriba el resultado en el campo adecuado.'
txt_test2 = 'Realice 30 sentadillas en 45 segundos. Para hacer esto haga clic en el botón "Empezar a hacer sentadillas" \npara iniciar el contador de sentadillas.'
txt_test3 = 'Acuéstese y tome su pulso los primeros 15 segundos del minuto, luego durante los últimos 15 segundos del minuto.\nPresione el botón "Iniciar prueba final" para iniciar al temporizador.\nLos segundos que deberían medirse se indican en verde y los segundos que no deben medirse se indican en negro. Escriba los resultados en los campos adecuados'
txt_sendresults = 'Enviar los resultados'
txt_hinttest1 = '0'
txt_hinttest2 = '0'
txt_hinttest3 = '0'
txt_starttest1 = 'Iniciar primera prueba'
txt_starttest2 = 'Empezar a hacer sentadillas'
txt_starttest3 = 'Iniciar prueba final'
time = QTime(0, 0, 15)
txt_timer = time.toString("hh:mm:ss")
txt_age = 'Años completos:'
txt_finalwin = 'Resultados'
txt_index = 'Índice de Ruffier:  '
txt_workheart = 'Rendimiento cardíaco:  '
txt_res1 = "bajo. ¡Acuda al médico de inmediato!"
txt_res2 = "satisfactorio. ¡Vea a su médico!"
txt_res3 = "promedio. Puede valer la pena ver a su médico para que lo revise."
txt_res4 = "por encima del promedio"
txt_res5 = "alto"