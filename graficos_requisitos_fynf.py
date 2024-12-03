import matplotlib.pyplot as plt
import numpy as np

def set_style():
    """
    Configura el estilo básico para todos los gráficos
    """
    plt.style.use('default')
    plt.rcParams['font.size'] = 10
    plt.rcParams['figure.figsize'] = (10, 6)
    plt.rcParams['axes.grid'] = True
    plt.rcParams['grid.alpha'] = 0.3

def create_requirements_chart():
    """
    Crea el gráfico de estado de requerimientos (barras agrupadas)
    """
    categories = ['Completado', 'En Progreso', 'Pendiente']
    functional = [10, 5, 2]  # Requerimientos funcionales
    non_functional = [8, 3, 4]  # Requerimientos no funcionales
    
    x = np.arange(len(categories))
    width = 0.35

    fig, ax = plt.subplots()
    bars1 = ax.bar(x - width/2, functional, width, label='Funcionales', color='#4287f5')
    bars2 = ax.bar(x + width/2, non_functional, width, label='No Funcionales', color='#f54242')

    ax.set_title('Estado de Requerimientos')
    ax.set_xlabel('Estado')
    ax.set_ylabel('Cantidad')
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.legend()

    # Agregar valores en las barras
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, height,
                   f'{int(height)}', ha='center', va='bottom')

    plt.tight_layout()
    plt.savefig('estado_de_requerimientos.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_test_cases_pie():
    """
    Crea el gráfico de proporción de casos de prueba (pie)
    """
    functionalities = ['Registro', 'Inicio de sesión', 'Recuperación\nde contraseña', 
                      'Panel cliente', 'Panel operador']
    test_cases = [10, 15, 5, 20, 12]
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

    fig, ax = plt.subplots()
    wedges, texts, autotexts = ax.pie(test_cases, labels=functionalities, 
                                     autopct='%1.1f%%', startangle=90, colors=colors)
    
    ax.set_title('Proporción de Casos de Prueba por Funcionalidad')
    
    plt.setp(autotexts, size=8, weight="bold")
    plt.setp(texts, size=9)
    
    plt.tight_layout()
    plt.savefig('proporcion_casos_de_prueba.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_test_cases_status():
    """
    Crea el gráfico de estado de casos de prueba (barras apiladas)
    """
    functionalities = ['Registro', 'Inicio de\nsesión', 'Recuperación\nde contraseña', 
                      'Panel\ncliente', 'Panel\noperador']
    executed_cases = [8, 12, 4, 18, 10]
    pending_cases = [2, 3, 1, 2, 2]

    fig, ax = plt.subplots()
    x = np.arange(len(functionalities))
    width = 0.8

    ax.bar(x, executed_cases, width, label='Ejecutados', color='#66b3ff')
    ax.bar(x, pending_cases, width, bottom=executed_cases, label='Pendientes', color='#ff9999')

    ax.set_title('Estado de Casos de Prueba por Funcionalidad')
    ax.set_xlabel('Funcionalidades')
    ax.set_ylabel('Número de Casos')
    ax.set_xticks(x)
    ax.set_xticklabels(functionalities)
    ax.legend()

    # Agregar valores en las barras
    for i in range(len(functionalities)):
        # Valor para casos ejecutados
        plt.text(x[i], executed_cases[i]/2, str(executed_cases[i]), 
                ha='center', va='center')
        # Valor para casos pendientes
        if pending_cases[i] > 0:
            plt.text(x[i], executed_cases[i] + pending_cases[i]/2, 
                    str(pending_cases[i]), ha='center', va='center')

    plt.tight_layout()
    plt.savefig('estado_casos_de_prueba.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_test_cycles_evolution():
    """
    Crea el gráfico de evolución de ciclos de prueba (líneas)
    """
    cycles = ['Ciclo 1', 'Ciclo 2', 'Ciclo 3', 'Ciclo 4', 'Ciclo 5']
    executed_cases = [20, 35, 50, 70, 90]
    approved_cases = [18, 30, 45, 65, 85]

    fig, ax = plt.subplots()
    
    # Crear líneas con marcadores
    ax.plot(cycles, executed_cases, marker='o', label='Casos Ejecutados', 
           color='#66b3ff', linewidth=2, markersize=8)
    ax.plot(cycles, approved_cases, marker='s', label='Casos Aprobados', 
           color='#ff9999', linewidth=2, markersize=8)

    ax.set_title('Evolución de los Ciclos de Prueba')
    ax.set_xlabel('Ciclos de Prueba')
    ax.set_ylabel('Número de Casos')
    ax.legend()

    # Agregar valores en los puntos
    for i, (e, a) in enumerate(zip(executed_cases, approved_cases)):
        ax.text(i, e + 2, str(e), ha='center')
        ax.text(i, a - 2, str(a), ha='center')

    plt.tight_layout()
    plt.savefig('evolucion_ciclos_prueba.png', dpi=300, bbox_inches='tight')
    plt.close()

def main():
    """
    Función principal que genera todos los gráficos
    """
    # Configurar el estilo general
    set_style()
    
    # Generar todos los gráficos
    create_requirements_chart()
    create_test_cases_pie()
    create_test_cases_status()
    create_test_cycles_evolution()
    
    print("Gráficos generados exitosamente.")

if __name__ == "__main__":
    main()