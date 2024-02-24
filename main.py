from insurancePP.pipeline.stage1_data_ingestion import DataIngestionTrainingPipeline
# from textSummerizer.pipeline.stage2_data_validation import DataValidationTrainingPipeline
# from textSummerizer.pipeline.stage3_data_transformation import DataTransformationTrainingPipeline
# from textSummerizer.pipeline.stage4_model_trainer import ModelTrainingPipeline
# from textSummerizer.pipeline.stage5_model_evaluation import ModelEvaluationPipeline
from insurancePP.logging import logger

STAGE_NAME = 'data_ingestion_training'
try:
    logger.info(f'>>>>> stage {STAGE_NAME} has started <<<<<')
    data_ingestion_training_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_training_pipeline.main()
    logger.info(f'>>>>> stage {STAGE_NAME} has completed <<<<<')
except Exception as e:
    logger.error(f'>>>>> stage {STAGE_NAME} has failed <<<<<')
    raise e
