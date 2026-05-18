from mlProject import logger

from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

from mlProject.config.dagshub_config import init_dagshub


def run_pipeline():
    try:
        # ---------------- DAGSHUB INIT (ONLY ONCE) ----------------
        init_dagshub()

        # ---------------- STAGE 1 ----------------
        logger.info(">>> Data Ingestion Stage started <<<")
        DataIngestionTrainingPipeline().main()
        logger.info(">>> Data Ingestion Stage completed <<<\n")

        # ---------------- STAGE 2 ----------------
        logger.info(">>> Data Validation Stage started <<<")
        DataValidationTrainingPipeline().main()
        logger.info(">>> Data Validation Stage completed <<<\n")

        # ---------------- STAGE 3 ----------------
        logger.info(">>> Data Transformation Stage started <<<")
        DataTransformationTrainingPipeline().main()
        logger.info(">>> Data Transformation Stage completed <<<\n")

        # ---------------- STAGE 4 ----------------
        logger.info(">>> Model Trainer Stage started <<<")
        ModelTrainerTrainingPipeline().main()
        logger.info(">>> Model Trainer Stage completed <<<\n")

        # ---------------- STAGE 5 ----------------
        logger.info(">>> Model Evaluation Stage started <<<")
        ModelEvaluationTrainingPipeline().main()
        logger.info(">>> Model Evaluation Stage completed <<<\n")

        logger.info("FULL PIPELINE EXECUTION COMPLETED")

    except Exception as e:
        logger.exception(e)
        raise e


if __name__ == "__main__":
    run_pipeline()