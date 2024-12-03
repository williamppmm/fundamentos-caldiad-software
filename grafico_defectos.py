import matplotlib.pyplot as plt
import numpy as np

def create_defects_by_severity():
    """
    Crea gráfico de defectos por severidad
    """
    severities = ['Crítico', 'Mayor', 'Menor', 'Trivial']
    defects = [2, 8, 15, 5]  # Total: 30 defectos
    colors = ['#ff4444', '#ffaa33', '#44bb55', '#aaaaaa']

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(severities, defects, color=colors)

    ax.set_title('Defectos por Nivel de Severidad')
    ax.set_xlabel('Severidad del Defecto')
    ax.set_ylabel('Número de Casos Reportados')

    # Agregar valores sobre las barras
    for bar in bars:
        height = bar.get_height()
        percentage = (height / sum(defects)) * 100
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}\n({percentage:.1f}%)',
                ha='center', va='bottom')

    plt.tight_layout()
    plt.savefig('defectos_por_severidad.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_improvement_opportunities():
    """
    Crea gráfico de oportunidades de mejora por categoría
    """
    categories = ['Rendimiento', 'Usabilidad', 'Seguridad', 
                 'Funcionalidad', 'Documentación']
    opportunities = [12, 8, 6, 15, 4]  # Total: 45 oportunidades
    colors = ['#4287f5', '#42f5a1', '#f542b9', '#f5d442', '#a142f5']

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(categories, opportunities, color=colors)

    ax.set_title('Oportunidades de Mejora por Categoría')
    ax.set_xlabel('Categoría')
    ax.set_ylabel('Número de Oportunidades')

    # Agregar valores sobre las barras
    for bar in bars:
        height = bar.get_height()
        percentage = (height / sum(opportunities)) * 100  # Corrección aquí
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}\n({percentage:.1f}%)',
                ha='center', va='bottom')

    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('oportunidades_mejora.png', dpi=300, bbox_inches='tight')
    plt.close()

def main():
    """
    Genera los gráficos de defectos y oportunidades de mejora
    """
    plt.style.use('default')
    plt.rcParams['font.size'] = 10
    plt.rcParams['figure.figsize'] = (10, 6)
    plt.rcParams['axes.grid'] = True
    plt.rcParams['grid.alpha'] = 0.3

    create_defects_by_severity()
    create_improvement_opportunities()
    print("Gráficos de defectos y oportunidades generados exitosamente.")

if __name__ == "__main__":
    main()