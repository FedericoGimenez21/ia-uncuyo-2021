from entorno import*
from agent import*



print("......")
print("       Entorno de Prueba")
#Enviroment(tamaño filas, tamaño columnas, probabilidad de suciedad)
EntornoPrueba=Enviroment(8,8,0.1)
EntornoPrueba.prin()


print(".......")
print(" ")




"AGENTE REFLEXIVO SIMPLE "
agenteRef=AgentReflexSimple(EntornoPrueba)
print("       AGENTE REFLEXIVO SIMPLE ya procesado")
agenteRef.think()
print("performance: ",agenteRef.e.get_performance())

#imprimimos el entorno

agenteRef.e.prin()


print("............")
"AGENTE CON ACCIONES RANDOM"



agente=AgentRandom(EntornoPrueba)

agente.think()

print("")
print("       AGENTE CON ACCIONES RANDOM ya procesado ")

print("performance: ",agente.e.get_performance())
agente.e.prin()
print("........")


print("       Entorno de Prueba")
EntornoPrueba.prin()

