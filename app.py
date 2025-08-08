"""Demo script for La Ruta Digital modules."""
from ruta_digital.learning import InteractiveLearningModule
from ruta_digital.life_plan import LifePlanGenerator
from ruta_digital.scam_alert import ScamAlertSystem
from ruta_digital.yola_experience import YolaExperience
from ruta_digital.monitoring import UserProgress


def main() -> None:
    lesson = InteractiveLearningModule(
        title="Identificar estafas",
        content_blocks=["Ejemplo de publicación sospechosa"],
        quizzes=["¿Qué harías?"],
    )
    lesson.run()

    planner = LifePlanGenerator()
    planner.add_goal("Estudiar programación", ["Investigar cursos", "Practicar diariamente"])
    print(planner.summary())

    scam = ScamAlertSystem()
    scam.report("Oferta de trabajo dudosa", confidence=0.8)
    print(f"Reportes registrados: {len(scam.reports)}")

    yola = YolaExperience()
    yola.play()

    progress = UserProgress()
    progress.pre_scores["module1"] = 1
    progress.post_scores["module1"] = 3
    print(f"Ganancia de conocimiento: {progress.gain('module1')}")


if __name__ == "__main__":
    main()
