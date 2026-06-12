import logging
import structlog

structlog.configure(
    processors=[structlog.processors.JSONRenderer()]
)
logger = structlog.get_logger()

logger.info('prediction_made', 
    model_id='v1',
    confidence=0.95,
    duration_ms=42)