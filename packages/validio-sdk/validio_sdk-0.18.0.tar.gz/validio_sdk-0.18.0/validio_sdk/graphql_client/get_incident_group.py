from datetime import datetime
from typing import Any, List, Literal, Optional, Union

from pydantic import Field

from validio_sdk.scalars import (
    JsonFilterExpression,
    JsonPointer,
    SegmentationId,
    SourceId,
    ValidatorId,
    WindowId,
)

from .base_model import BaseModel
from .enums import (
    CategoricalDistributionMetric,
    ComparisonOperator,
    DecisionBoundsType,
    IncidentGroupPriority,
    IncidentStatus,
    NumericAnomalyMetric,
    NumericDistributionMetric,
    NumericMetric,
    RelativeTimeMetric,
    RelativeVolumeMetric,
    VolumeMetric,
)
from .fragments import SegmentDetails


class GetIncidentGroup(BaseModel):
    incident_group: Optional["GetIncidentGroupIncidentGroup"] = Field(
        alias="incidentGroup"
    )


class GetIncidentGroupIncidentGroup(BaseModel):
    id: Any
    status: IncidentStatus
    priority: IncidentGroupPriority
    owner: Optional["GetIncidentGroupIncidentGroupOwner"]
    source: "GetIncidentGroupIncidentGroupSource"
    validator: Union[
        "GetIncidentGroupIncidentGroupValidatorValidator",
        "GetIncidentGroupIncidentGroupValidatorCategoricalDistributionValidator",
        "GetIncidentGroupIncidentGroupValidatorFreshnessValidator",
        "GetIncidentGroupIncidentGroupValidatorNumericAnomalyValidator",
        "GetIncidentGroupIncidentGroupValidatorNumericDistributionValidator",
        "GetIncidentGroupIncidentGroupValidatorNumericValidator",
        "GetIncidentGroupIncidentGroupValidatorRelativeTimeValidator",
        "GetIncidentGroupIncidentGroupValidatorRelativeVolumeValidator",
        "GetIncidentGroupIncidentGroupValidatorSqlValidator",
        "GetIncidentGroupIncidentGroupValidatorVolumeValidator",
    ] = Field(discriminator="typename__")
    segment: "GetIncidentGroupIncidentGroupSegment"
    severity_stats: "GetIncidentGroupIncidentGroupSeverityStats" = Field(
        alias="severityStats"
    )
    first_seen_at: datetime = Field(alias="firstSeenAt")
    last_seen_at: datetime = Field(alias="lastSeenAt")


class GetIncidentGroupIncidentGroupOwner(BaseModel):
    id: str
    display_name: str = Field(alias="displayName")


class GetIncidentGroupIncidentGroupSource(BaseModel):
    typename__: Literal[
        "AwsAthenaSource",
        "AwsKinesisSource",
        "AwsRedshiftSource",
        "AwsS3Source",
        "AzureSynapseSource",
        "ClickHouseSource",
        "DatabricksSource",
        "DbtModelRunSource",
        "DbtTestResultSource",
        "DemoSource",
        "GcpBigQuerySource",
        "GcpPubSubLiteSource",
        "GcpPubSubSource",
        "GcpStorageSource",
        "KafkaSource",
        "PostgreSqlSource",
        "SnowflakeSource",
        "Source",
    ] = Field(alias="__typename")
    id: SourceId
    name: str


class GetIncidentGroupIncidentGroupValidatorValidator(BaseModel):
    typename__: Literal["Validator"] = Field(alias="__typename")
    id: ValidatorId
    name: str
    has_custom_name: bool = Field(alias="hasCustomName")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    source_config: "GetIncidentGroupIncidentGroupValidatorValidatorSourceConfig" = (
        Field(alias="sourceConfig")
    )
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")
    resource_namespace: str = Field(alias="resourceNamespace")


class GetIncidentGroupIncidentGroupValidatorValidatorSourceConfig(BaseModel):
    source: "GetIncidentGroupIncidentGroupValidatorValidatorSourceConfigSource"
    window: "GetIncidentGroupIncidentGroupValidatorValidatorSourceConfigWindow"
    segmentation: (
        "GetIncidentGroupIncidentGroupValidatorValidatorSourceConfigSegmentation"
    )
    filter: Optional[JsonFilterExpression]


class GetIncidentGroupIncidentGroupValidatorValidatorSourceConfigSource(BaseModel):
    typename__: Literal[
        "AwsAthenaSource",
        "AwsKinesisSource",
        "AwsRedshiftSource",
        "AwsS3Source",
        "AzureSynapseSource",
        "ClickHouseSource",
        "DatabricksSource",
        "DbtModelRunSource",
        "DbtTestResultSource",
        "DemoSource",
        "GcpBigQuerySource",
        "GcpPubSubLiteSource",
        "GcpPubSubSource",
        "GcpStorageSource",
        "KafkaSource",
        "PostgreSqlSource",
        "SnowflakeSource",
        "Source",
    ] = Field(alias="__typename")
    id: SourceId
    name: str
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")


class GetIncidentGroupIncidentGroupValidatorValidatorSourceConfigWindow(BaseModel):
    typename__: Literal[
        "FileWindow", "FixedBatchWindow", "GlobalWindow", "TumblingWindow", "Window"
    ] = Field(alias="__typename")
    id: WindowId
    name: str
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")


class GetIncidentGroupIncidentGroupValidatorValidatorSourceConfigSegmentation(
    BaseModel
):
    typename__: Literal["Segmentation"] = Field(alias="__typename")
    id: SegmentationId
    name: str
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")


class GetIncidentGroupIncidentGroupValidatorCategoricalDistributionValidator(BaseModel):
    typename__: Literal["CategoricalDistributionValidator"] = Field(alias="__typename")
    id: ValidatorId
    name: str
    has_custom_name: bool = Field(alias="hasCustomName")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    source_config: (
        "GetIncidentGroupIncidentGroupValidatorCategoricalDistributionValidatorSourceConfig"
    ) = Field(alias="sourceConfig")
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")
    resource_namespace: str = Field(alias="resourceNamespace")
    config: (
        "GetIncidentGroupIncidentGroupValidatorCategoricalDistributionValidatorConfig"
    )
    reference_source_config: (
        "GetIncidentGroupIncidentGroupValidatorCategoricalDistributionValidatorReferenceSourceConfig"
    ) = Field(alias="referenceSourceConfig")


class GetIncidentGroupIncidentGroupValidatorCategoricalDistributionValidatorSourceConfig(
    BaseModel
):
    source: "GetIncidentGroupIncidentGroupValidatorCategoricalDistributionValidatorSourceConfigSource"
    window: "GetIncidentGroupIncidentGroupValidatorCategoricalDistributionValidatorSourceConfigWindow"
    segmentation: "GetIncidentGroupIncidentGroupValidatorCategoricalDistributionValidatorSourceConfigSegmentation"
    filter: Optional[JsonFilterExpression]


class GetIncidentGroupIncidentGroupValidatorCategoricalDistributionValidatorSourceConfigSource(
    BaseModel
):
    typename__: Literal[
        "AwsAthenaSource",
        "AwsKinesisSource",
        "AwsRedshiftSource",
        "AwsS3Source",
        "AzureSynapseSource",
        "ClickHouseSource",
        "DatabricksSource",
        "DbtModelRunSource",
        "DbtTestResultSource",
        "DemoSource",
        "GcpBigQuerySource",
        "GcpPubSubLiteSource",
        "GcpPubSubSource",
        "GcpStorageSource",
        "KafkaSource",
        "PostgreSqlSource",
        "SnowflakeSource",
        "Source",
    ] = Field(alias="__typename")
    id: SourceId
    name: str
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")


class GetIncidentGroupIncidentGroupValidatorCategoricalDistributionValidatorSourceConfigWindow(
    BaseModel
):
    typename__: Literal[
        "FileWindow", "FixedBatchWindow", "GlobalWindow", "TumblingWindow", "Window"
    ] = Field(alias="__typename")
    id: WindowId
    name: str
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")


class GetIncidentGroupIncidentGroupValidatorCategoricalDistributionValidatorSourceConfigSegmentation(
    BaseModel
):
    typename__: Literal["Segmentation"] = Field(alias="__typename")
    id: SegmentationId
    name: str
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")


class GetIncidentGroupIncidentGroupValidatorCategoricalDistributionValidatorConfig(
    BaseModel
):
    source_field: JsonPointer = Field(alias="sourceField")
    reference_source_field: JsonPointer = Field(alias="referenceSourceField")
    categorical_distribution_metric: CategoricalDistributionMetric = Field(
        alias="categoricalDistributionMetric"
    )
    initialize_with_backfill: bool = Field(alias="initializeWithBackfill")
    threshold: Union[
        "GetIncidentGroupIncidentGroupValidatorCategoricalDistributionValidatorConfigThresholdDynamicThreshold",
        "GetIncidentGroupIncidentGroupValidatorCategoricalDistributionValidatorConfigThresholdFixedThreshold",
    ] = Field(discriminator="typename__")


class GetIncidentGroupIncidentGroupValidatorCategoricalDistributionValidatorConfigThresholdDynamicThreshold(
    BaseModel
):
    typename__: Literal["DynamicThreshold"] = Field(alias="__typename")
    sensitivity: float
    decision_bounds_type: Optional[DecisionBoundsType] = Field(
        alias="decisionBoundsType"
    )


class GetIncidentGroupIncidentGroupValidatorCategoricalDistributionValidatorConfigThresholdFixedThreshold(
    BaseModel
):
    typename__: Literal["FixedThreshold"] = Field(alias="__typename")
    operator: ComparisonOperator
    value: float


class GetIncidentGroupIncidentGroupValidatorCategoricalDistributionValidatorReferenceSourceConfig(
    BaseModel
):
    source: "GetIncidentGroupIncidentGroupValidatorCategoricalDistributionValidatorReferenceSourceConfigSource"
    window: "GetIncidentGroupIncidentGroupValidatorCategoricalDistributionValidatorReferenceSourceConfigWindow"
    history: int
    offset: int
    filter: Optional[JsonFilterExpression]


class GetIncidentGroupIncidentGroupValidatorCategoricalDistributionValidatorReferenceSourceConfigSource(
    BaseModel
):
    typename__: Literal[
        "AwsAthenaSource",
        "AwsKinesisSource",
        "AwsRedshiftSource",
        "AwsS3Source",
        "AzureSynapseSource",
        "ClickHouseSource",
        "DatabricksSource",
        "DbtModelRunSource",
        "DbtTestResultSource",
        "DemoSource",
        "GcpBigQuerySource",
        "GcpPubSubLiteSource",
        "GcpPubSubSource",
        "GcpStorageSource",
        "KafkaSource",
        "PostgreSqlSource",
        "SnowflakeSource",
        "Source",
    ] = Field(alias="__typename")
    id: SourceId
    name: str
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")


class GetIncidentGroupIncidentGroupValidatorCategoricalDistributionValidatorReferenceSourceConfigWindow(
    BaseModel
):
    typename__: Literal[
        "FileWindow", "FixedBatchWindow", "GlobalWindow", "TumblingWindow", "Window"
    ] = Field(alias="__typename")
    id: WindowId
    name: str
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")


class GetIncidentGroupIncidentGroupValidatorFreshnessValidator(BaseModel):
    typename__: Literal["FreshnessValidator"] = Field(alias="__typename")
    id: ValidatorId
    name: str
    has_custom_name: bool = Field(alias="hasCustomName")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    source_config: (
        "GetIncidentGroupIncidentGroupValidatorFreshnessValidatorSourceConfig"
    ) = Field(alias="sourceConfig")
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")
    resource_namespace: str = Field(alias="resourceNamespace")
    config: "GetIncidentGroupIncidentGroupValidatorFreshnessValidatorConfig"


class GetIncidentGroupIncidentGroupValidatorFreshnessValidatorSourceConfig(BaseModel):
    source: "GetIncidentGroupIncidentGroupValidatorFreshnessValidatorSourceConfigSource"
    window: "GetIncidentGroupIncidentGroupValidatorFreshnessValidatorSourceConfigWindow"
    segmentation: "GetIncidentGroupIncidentGroupValidatorFreshnessValidatorSourceConfigSegmentation"
    filter: Optional[JsonFilterExpression]


class GetIncidentGroupIncidentGroupValidatorFreshnessValidatorSourceConfigSource(
    BaseModel
):
    typename__: Literal[
        "AwsAthenaSource",
        "AwsKinesisSource",
        "AwsRedshiftSource",
        "AwsS3Source",
        "AzureSynapseSource",
        "ClickHouseSource",
        "DatabricksSource",
        "DbtModelRunSource",
        "DbtTestResultSource",
        "DemoSource",
        "GcpBigQuerySource",
        "GcpPubSubLiteSource",
        "GcpPubSubSource",
        "GcpStorageSource",
        "KafkaSource",
        "PostgreSqlSource",
        "SnowflakeSource",
        "Source",
    ] = Field(alias="__typename")
    id: SourceId
    name: str
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")


class GetIncidentGroupIncidentGroupValidatorFreshnessValidatorSourceConfigWindow(
    BaseModel
):
    typename__: Literal[
        "FileWindow", "FixedBatchWindow", "GlobalWindow", "TumblingWindow", "Window"
    ] = Field(alias="__typename")
    id: WindowId
    name: str
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")


class GetIncidentGroupIncidentGroupValidatorFreshnessValidatorSourceConfigSegmentation(
    BaseModel
):
    typename__: Literal["Segmentation"] = Field(alias="__typename")
    id: SegmentationId
    name: str
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")


class GetIncidentGroupIncidentGroupValidatorFreshnessValidatorConfig(BaseModel):
    initialize_with_backfill: bool = Field(alias="initializeWithBackfill")
    optional_source_field: Optional[JsonPointer] = Field(alias="optionalSourceField")
    threshold: Union[
        "GetIncidentGroupIncidentGroupValidatorFreshnessValidatorConfigThresholdDynamicThreshold",
        "GetIncidentGroupIncidentGroupValidatorFreshnessValidatorConfigThresholdFixedThreshold",
    ] = Field(discriminator="typename__")


class GetIncidentGroupIncidentGroupValidatorFreshnessValidatorConfigThresholdDynamicThreshold(
    BaseModel
):
    typename__: Literal["DynamicThreshold"] = Field(alias="__typename")
    sensitivity: float
    decision_bounds_type: Optional[DecisionBoundsType] = Field(
        alias="decisionBoundsType"
    )


class GetIncidentGroupIncidentGroupValidatorFreshnessValidatorConfigThresholdFixedThreshold(
    BaseModel
):
    typename__: Literal["FixedThreshold"] = Field(alias="__typename")
    operator: ComparisonOperator
    value: float


class GetIncidentGroupIncidentGroupValidatorNumericAnomalyValidator(BaseModel):
    typename__: Literal["NumericAnomalyValidator"] = Field(alias="__typename")
    id: ValidatorId
    name: str
    has_custom_name: bool = Field(alias="hasCustomName")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    source_config: (
        "GetIncidentGroupIncidentGroupValidatorNumericAnomalyValidatorSourceConfig"
    ) = Field(alias="sourceConfig")
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")
    resource_namespace: str = Field(alias="resourceNamespace")
    config: "GetIncidentGroupIncidentGroupValidatorNumericAnomalyValidatorConfig"
    reference_source_config: (
        "GetIncidentGroupIncidentGroupValidatorNumericAnomalyValidatorReferenceSourceConfig"
    ) = Field(alias="referenceSourceConfig")


class GetIncidentGroupIncidentGroupValidatorNumericAnomalyValidatorSourceConfig(
    BaseModel
):
    source: "GetIncidentGroupIncidentGroupValidatorNumericAnomalyValidatorSourceConfigSource"
    window: "GetIncidentGroupIncidentGroupValidatorNumericAnomalyValidatorSourceConfigWindow"
    segmentation: "GetIncidentGroupIncidentGroupValidatorNumericAnomalyValidatorSourceConfigSegmentation"
    filter: Optional[JsonFilterExpression]


class GetIncidentGroupIncidentGroupValidatorNumericAnomalyValidatorSourceConfigSource(
    BaseModel
):
    typename__: Literal[
        "AwsAthenaSource",
        "AwsKinesisSource",
        "AwsRedshiftSource",
        "AwsS3Source",
        "AzureSynapseSource",
        "ClickHouseSource",
        "DatabricksSource",
        "DbtModelRunSource",
        "DbtTestResultSource",
        "DemoSource",
        "GcpBigQuerySource",
        "GcpPubSubLiteSource",
        "GcpPubSubSource",
        "GcpStorageSource",
        "KafkaSource",
        "PostgreSqlSource",
        "SnowflakeSource",
        "Source",
    ] = Field(alias="__typename")
    id: SourceId
    name: str
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")


class GetIncidentGroupIncidentGroupValidatorNumericAnomalyValidatorSourceConfigWindow(
    BaseModel
):
    typename__: Literal[
        "FileWindow", "FixedBatchWindow", "GlobalWindow", "TumblingWindow", "Window"
    ] = Field(alias="__typename")
    id: WindowId
    name: str
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")


class GetIncidentGroupIncidentGroupValidatorNumericAnomalyValidatorSourceConfigSegmentation(
    BaseModel
):
    typename__: Literal["Segmentation"] = Field(alias="__typename")
    id: SegmentationId
    name: str
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")


class GetIncidentGroupIncidentGroupValidatorNumericAnomalyValidatorConfig(BaseModel):
    source_field: JsonPointer = Field(alias="sourceField")
    numeric_anomaly_metric: NumericAnomalyMetric = Field(alias="numericAnomalyMetric")
    initialize_with_backfill: bool = Field(alias="initializeWithBackfill")
    threshold: Union[
        "GetIncidentGroupIncidentGroupValidatorNumericAnomalyValidatorConfigThresholdDynamicThreshold",
        "GetIncidentGroupIncidentGroupValidatorNumericAnomalyValidatorConfigThresholdFixedThreshold",
    ] = Field(discriminator="typename__")
    reference_source_field: JsonPointer = Field(alias="referenceSourceField")
    sensitivity: float
    minimum_reference_datapoints: Optional[float] = Field(
        alias="minimumReferenceDatapoints"
    )
    minimum_absolute_difference: float = Field(alias="minimumAbsoluteDifference")
    minimum_relative_difference_percent: float = Field(
        alias="minimumRelativeDifferencePercent"
    )


class GetIncidentGroupIncidentGroupValidatorNumericAnomalyValidatorConfigThresholdDynamicThreshold(
    BaseModel
):
    typename__: Literal["DynamicThreshold"] = Field(alias="__typename")
    sensitivity: float
    decision_bounds_type: Optional[DecisionBoundsType] = Field(
        alias="decisionBoundsType"
    )


class GetIncidentGroupIncidentGroupValidatorNumericAnomalyValidatorConfigThresholdFixedThreshold(
    BaseModel
):
    typename__: Literal["FixedThreshold"] = Field(alias="__typename")
    operator: ComparisonOperator
    value: float


class GetIncidentGroupIncidentGroupValidatorNumericAnomalyValidatorReferenceSourceConfig(
    BaseModel
):
    source: "GetIncidentGroupIncidentGroupValidatorNumericAnomalyValidatorReferenceSourceConfigSource"
    window: "GetIncidentGroupIncidentGroupValidatorNumericAnomalyValidatorReferenceSourceConfigWindow"
    history: int
    offset: int
    filter: Optional[JsonFilterExpression]


class GetIncidentGroupIncidentGroupValidatorNumericAnomalyValidatorReferenceSourceConfigSource(
    BaseModel
):
    typename__: Literal[
        "AwsAthenaSource",
        "AwsKinesisSource",
        "AwsRedshiftSource",
        "AwsS3Source",
        "AzureSynapseSource",
        "ClickHouseSource",
        "DatabricksSource",
        "DbtModelRunSource",
        "DbtTestResultSource",
        "DemoSource",
        "GcpBigQuerySource",
        "GcpPubSubLiteSource",
        "GcpPubSubSource",
        "GcpStorageSource",
        "KafkaSource",
        "PostgreSqlSource",
        "SnowflakeSource",
        "Source",
    ] = Field(alias="__typename")
    id: SourceId
    name: str
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")


class GetIncidentGroupIncidentGroupValidatorNumericAnomalyValidatorReferenceSourceConfigWindow(
    BaseModel
):
    typename__: Literal[
        "FileWindow", "FixedBatchWindow", "GlobalWindow", "TumblingWindow", "Window"
    ] = Field(alias="__typename")
    id: WindowId
    name: str
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")


class GetIncidentGroupIncidentGroupValidatorNumericDistributionValidator(BaseModel):
    typename__: Literal["NumericDistributionValidator"] = Field(alias="__typename")
    id: ValidatorId
    name: str
    has_custom_name: bool = Field(alias="hasCustomName")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    source_config: (
        "GetIncidentGroupIncidentGroupValidatorNumericDistributionValidatorSourceConfig"
    ) = Field(alias="sourceConfig")
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")
    resource_namespace: str = Field(alias="resourceNamespace")
    config: "GetIncidentGroupIncidentGroupValidatorNumericDistributionValidatorConfig"
    reference_source_config: (
        "GetIncidentGroupIncidentGroupValidatorNumericDistributionValidatorReferenceSourceConfig"
    ) = Field(alias="referenceSourceConfig")


class GetIncidentGroupIncidentGroupValidatorNumericDistributionValidatorSourceConfig(
    BaseModel
):
    source: "GetIncidentGroupIncidentGroupValidatorNumericDistributionValidatorSourceConfigSource"
    window: "GetIncidentGroupIncidentGroupValidatorNumericDistributionValidatorSourceConfigWindow"
    segmentation: "GetIncidentGroupIncidentGroupValidatorNumericDistributionValidatorSourceConfigSegmentation"
    filter: Optional[JsonFilterExpression]


class GetIncidentGroupIncidentGroupValidatorNumericDistributionValidatorSourceConfigSource(
    BaseModel
):
    typename__: Literal[
        "AwsAthenaSource",
        "AwsKinesisSource",
        "AwsRedshiftSource",
        "AwsS3Source",
        "AzureSynapseSource",
        "ClickHouseSource",
        "DatabricksSource",
        "DbtModelRunSource",
        "DbtTestResultSource",
        "DemoSource",
        "GcpBigQuerySource",
        "GcpPubSubLiteSource",
        "GcpPubSubSource",
        "GcpStorageSource",
        "KafkaSource",
        "PostgreSqlSource",
        "SnowflakeSource",
        "Source",
    ] = Field(alias="__typename")
    id: SourceId
    name: str
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")


class GetIncidentGroupIncidentGroupValidatorNumericDistributionValidatorSourceConfigWindow(
    BaseModel
):
    typename__: Literal[
        "FileWindow", "FixedBatchWindow", "GlobalWindow", "TumblingWindow", "Window"
    ] = Field(alias="__typename")
    id: WindowId
    name: str
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")


class GetIncidentGroupIncidentGroupValidatorNumericDistributionValidatorSourceConfigSegmentation(
    BaseModel
):
    typename__: Literal["Segmentation"] = Field(alias="__typename")
    id: SegmentationId
    name: str
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")


class GetIncidentGroupIncidentGroupValidatorNumericDistributionValidatorConfig(
    BaseModel
):
    source_field: JsonPointer = Field(alias="sourceField")
    reference_source_field: JsonPointer = Field(alias="referenceSourceField")
    distribution_metric: NumericDistributionMetric = Field(alias="distributionMetric")
    initialize_with_backfill: bool = Field(alias="initializeWithBackfill")
    threshold: Union[
        "GetIncidentGroupIncidentGroupValidatorNumericDistributionValidatorConfigThresholdDynamicThreshold",
        "GetIncidentGroupIncidentGroupValidatorNumericDistributionValidatorConfigThresholdFixedThreshold",
    ] = Field(discriminator="typename__")


class GetIncidentGroupIncidentGroupValidatorNumericDistributionValidatorConfigThresholdDynamicThreshold(
    BaseModel
):
    typename__: Literal["DynamicThreshold"] = Field(alias="__typename")
    sensitivity: float
    decision_bounds_type: Optional[DecisionBoundsType] = Field(
        alias="decisionBoundsType"
    )


class GetIncidentGroupIncidentGroupValidatorNumericDistributionValidatorConfigThresholdFixedThreshold(
    BaseModel
):
    typename__: Literal["FixedThreshold"] = Field(alias="__typename")
    operator: ComparisonOperator
    value: float


class GetIncidentGroupIncidentGroupValidatorNumericDistributionValidatorReferenceSourceConfig(
    BaseModel
):
    source: "GetIncidentGroupIncidentGroupValidatorNumericDistributionValidatorReferenceSourceConfigSource"
    window: "GetIncidentGroupIncidentGroupValidatorNumericDistributionValidatorReferenceSourceConfigWindow"
    history: int
    offset: int
    filter: Optional[JsonFilterExpression]


class GetIncidentGroupIncidentGroupValidatorNumericDistributionValidatorReferenceSourceConfigSource(
    BaseModel
):
    typename__: Literal[
        "AwsAthenaSource",
        "AwsKinesisSource",
        "AwsRedshiftSource",
        "AwsS3Source",
        "AzureSynapseSource",
        "ClickHouseSource",
        "DatabricksSource",
        "DbtModelRunSource",
        "DbtTestResultSource",
        "DemoSource",
        "GcpBigQuerySource",
        "GcpPubSubLiteSource",
        "GcpPubSubSource",
        "GcpStorageSource",
        "KafkaSource",
        "PostgreSqlSource",
        "SnowflakeSource",
        "Source",
    ] = Field(alias="__typename")
    id: SourceId
    name: str
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")


class GetIncidentGroupIncidentGroupValidatorNumericDistributionValidatorReferenceSourceConfigWindow(
    BaseModel
):
    typename__: Literal[
        "FileWindow", "FixedBatchWindow", "GlobalWindow", "TumblingWindow", "Window"
    ] = Field(alias="__typename")
    id: WindowId
    name: str
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")


class GetIncidentGroupIncidentGroupValidatorNumericValidator(BaseModel):
    typename__: Literal["NumericValidator"] = Field(alias="__typename")
    id: ValidatorId
    name: str
    has_custom_name: bool = Field(alias="hasCustomName")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    source_config: (
        "GetIncidentGroupIncidentGroupValidatorNumericValidatorSourceConfig"
    ) = Field(alias="sourceConfig")
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")
    resource_namespace: str = Field(alias="resourceNamespace")
    config: "GetIncidentGroupIncidentGroupValidatorNumericValidatorConfig"


class GetIncidentGroupIncidentGroupValidatorNumericValidatorSourceConfig(BaseModel):
    source: "GetIncidentGroupIncidentGroupValidatorNumericValidatorSourceConfigSource"
    window: "GetIncidentGroupIncidentGroupValidatorNumericValidatorSourceConfigWindow"
    segmentation: (
        "GetIncidentGroupIncidentGroupValidatorNumericValidatorSourceConfigSegmentation"
    )
    filter: Optional[JsonFilterExpression]


class GetIncidentGroupIncidentGroupValidatorNumericValidatorSourceConfigSource(
    BaseModel
):
    typename__: Literal[
        "AwsAthenaSource",
        "AwsKinesisSource",
        "AwsRedshiftSource",
        "AwsS3Source",
        "AzureSynapseSource",
        "ClickHouseSource",
        "DatabricksSource",
        "DbtModelRunSource",
        "DbtTestResultSource",
        "DemoSource",
        "GcpBigQuerySource",
        "GcpPubSubLiteSource",
        "GcpPubSubSource",
        "GcpStorageSource",
        "KafkaSource",
        "PostgreSqlSource",
        "SnowflakeSource",
        "Source",
    ] = Field(alias="__typename")
    id: SourceId
    name: str
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")


class GetIncidentGroupIncidentGroupValidatorNumericValidatorSourceConfigWindow(
    BaseModel
):
    typename__: Literal[
        "FileWindow", "FixedBatchWindow", "GlobalWindow", "TumblingWindow", "Window"
    ] = Field(alias="__typename")
    id: WindowId
    name: str
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")


class GetIncidentGroupIncidentGroupValidatorNumericValidatorSourceConfigSegmentation(
    BaseModel
):
    typename__: Literal["Segmentation"] = Field(alias="__typename")
    id: SegmentationId
    name: str
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")


class GetIncidentGroupIncidentGroupValidatorNumericValidatorConfig(BaseModel):
    source_field: JsonPointer = Field(alias="sourceField")
    metric: NumericMetric
    initialize_with_backfill: bool = Field(alias="initializeWithBackfill")
    threshold: Union[
        "GetIncidentGroupIncidentGroupValidatorNumericValidatorConfigThresholdDynamicThreshold",
        "GetIncidentGroupIncidentGroupValidatorNumericValidatorConfigThresholdFixedThreshold",
    ] = Field(discriminator="typename__")


class GetIncidentGroupIncidentGroupValidatorNumericValidatorConfigThresholdDynamicThreshold(
    BaseModel
):
    typename__: Literal["DynamicThreshold"] = Field(alias="__typename")
    sensitivity: float
    decision_bounds_type: Optional[DecisionBoundsType] = Field(
        alias="decisionBoundsType"
    )


class GetIncidentGroupIncidentGroupValidatorNumericValidatorConfigThresholdFixedThreshold(
    BaseModel
):
    typename__: Literal["FixedThreshold"] = Field(alias="__typename")
    operator: ComparisonOperator
    value: float


class GetIncidentGroupIncidentGroupValidatorRelativeTimeValidator(BaseModel):
    typename__: Literal["RelativeTimeValidator"] = Field(alias="__typename")
    id: ValidatorId
    name: str
    has_custom_name: bool = Field(alias="hasCustomName")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    source_config: (
        "GetIncidentGroupIncidentGroupValidatorRelativeTimeValidatorSourceConfig"
    ) = Field(alias="sourceConfig")
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")
    resource_namespace: str = Field(alias="resourceNamespace")
    config: "GetIncidentGroupIncidentGroupValidatorRelativeTimeValidatorConfig"


class GetIncidentGroupIncidentGroupValidatorRelativeTimeValidatorSourceConfig(
    BaseModel
):
    source: (
        "GetIncidentGroupIncidentGroupValidatorRelativeTimeValidatorSourceConfigSource"
    )
    window: (
        "GetIncidentGroupIncidentGroupValidatorRelativeTimeValidatorSourceConfigWindow"
    )
    segmentation: "GetIncidentGroupIncidentGroupValidatorRelativeTimeValidatorSourceConfigSegmentation"
    filter: Optional[JsonFilterExpression]


class GetIncidentGroupIncidentGroupValidatorRelativeTimeValidatorSourceConfigSource(
    BaseModel
):
    typename__: Literal[
        "AwsAthenaSource",
        "AwsKinesisSource",
        "AwsRedshiftSource",
        "AwsS3Source",
        "AzureSynapseSource",
        "ClickHouseSource",
        "DatabricksSource",
        "DbtModelRunSource",
        "DbtTestResultSource",
        "DemoSource",
        "GcpBigQuerySource",
        "GcpPubSubLiteSource",
        "GcpPubSubSource",
        "GcpStorageSource",
        "KafkaSource",
        "PostgreSqlSource",
        "SnowflakeSource",
        "Source",
    ] = Field(alias="__typename")
    id: SourceId
    name: str
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")


class GetIncidentGroupIncidentGroupValidatorRelativeTimeValidatorSourceConfigWindow(
    BaseModel
):
    typename__: Literal[
        "FileWindow", "FixedBatchWindow", "GlobalWindow", "TumblingWindow", "Window"
    ] = Field(alias="__typename")
    id: WindowId
    name: str
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")


class GetIncidentGroupIncidentGroupValidatorRelativeTimeValidatorSourceConfigSegmentation(
    BaseModel
):
    typename__: Literal["Segmentation"] = Field(alias="__typename")
    id: SegmentationId
    name: str
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")


class GetIncidentGroupIncidentGroupValidatorRelativeTimeValidatorConfig(BaseModel):
    source_field_minuend: JsonPointer = Field(alias="sourceFieldMinuend")
    source_field_subtrahend: JsonPointer = Field(alias="sourceFieldSubtrahend")
    relative_time_metric: RelativeTimeMetric = Field(alias="relativeTimeMetric")
    initialize_with_backfill: bool = Field(alias="initializeWithBackfill")
    threshold: Union[
        "GetIncidentGroupIncidentGroupValidatorRelativeTimeValidatorConfigThresholdDynamicThreshold",
        "GetIncidentGroupIncidentGroupValidatorRelativeTimeValidatorConfigThresholdFixedThreshold",
    ] = Field(discriminator="typename__")


class GetIncidentGroupIncidentGroupValidatorRelativeTimeValidatorConfigThresholdDynamicThreshold(
    BaseModel
):
    typename__: Literal["DynamicThreshold"] = Field(alias="__typename")
    sensitivity: float
    decision_bounds_type: Optional[DecisionBoundsType] = Field(
        alias="decisionBoundsType"
    )


class GetIncidentGroupIncidentGroupValidatorRelativeTimeValidatorConfigThresholdFixedThreshold(
    BaseModel
):
    typename__: Literal["FixedThreshold"] = Field(alias="__typename")
    operator: ComparisonOperator
    value: float


class GetIncidentGroupIncidentGroupValidatorRelativeVolumeValidator(BaseModel):
    typename__: Literal["RelativeVolumeValidator"] = Field(alias="__typename")
    id: ValidatorId
    name: str
    has_custom_name: bool = Field(alias="hasCustomName")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    source_config: (
        "GetIncidentGroupIncidentGroupValidatorRelativeVolumeValidatorSourceConfig"
    ) = Field(alias="sourceConfig")
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")
    resource_namespace: str = Field(alias="resourceNamespace")
    config: "GetIncidentGroupIncidentGroupValidatorRelativeVolumeValidatorConfig"
    reference_source_config: (
        "GetIncidentGroupIncidentGroupValidatorRelativeVolumeValidatorReferenceSourceConfig"
    ) = Field(alias="referenceSourceConfig")


class GetIncidentGroupIncidentGroupValidatorRelativeVolumeValidatorSourceConfig(
    BaseModel
):
    source: "GetIncidentGroupIncidentGroupValidatorRelativeVolumeValidatorSourceConfigSource"
    window: "GetIncidentGroupIncidentGroupValidatorRelativeVolumeValidatorSourceConfigWindow"
    segmentation: "GetIncidentGroupIncidentGroupValidatorRelativeVolumeValidatorSourceConfigSegmentation"
    filter: Optional[JsonFilterExpression]


class GetIncidentGroupIncidentGroupValidatorRelativeVolumeValidatorSourceConfigSource(
    BaseModel
):
    typename__: Literal[
        "AwsAthenaSource",
        "AwsKinesisSource",
        "AwsRedshiftSource",
        "AwsS3Source",
        "AzureSynapseSource",
        "ClickHouseSource",
        "DatabricksSource",
        "DbtModelRunSource",
        "DbtTestResultSource",
        "DemoSource",
        "GcpBigQuerySource",
        "GcpPubSubLiteSource",
        "GcpPubSubSource",
        "GcpStorageSource",
        "KafkaSource",
        "PostgreSqlSource",
        "SnowflakeSource",
        "Source",
    ] = Field(alias="__typename")
    id: SourceId
    name: str
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")


class GetIncidentGroupIncidentGroupValidatorRelativeVolumeValidatorSourceConfigWindow(
    BaseModel
):
    typename__: Literal[
        "FileWindow", "FixedBatchWindow", "GlobalWindow", "TumblingWindow", "Window"
    ] = Field(alias="__typename")
    id: WindowId
    name: str
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")


class GetIncidentGroupIncidentGroupValidatorRelativeVolumeValidatorSourceConfigSegmentation(
    BaseModel
):
    typename__: Literal["Segmentation"] = Field(alias="__typename")
    id: SegmentationId
    name: str
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")


class GetIncidentGroupIncidentGroupValidatorRelativeVolumeValidatorConfig(BaseModel):
    optional_source_field: Optional[JsonPointer] = Field(alias="optionalSourceField")
    optional_reference_source_field: Optional[JsonPointer] = Field(
        alias="optionalReferenceSourceField"
    )
    relative_volume_metric: RelativeVolumeMetric = Field(alias="relativeVolumeMetric")
    initialize_with_backfill: bool = Field(alias="initializeWithBackfill")
    threshold: Union[
        "GetIncidentGroupIncidentGroupValidatorRelativeVolumeValidatorConfigThresholdDynamicThreshold",
        "GetIncidentGroupIncidentGroupValidatorRelativeVolumeValidatorConfigThresholdFixedThreshold",
    ] = Field(discriminator="typename__")


class GetIncidentGroupIncidentGroupValidatorRelativeVolumeValidatorConfigThresholdDynamicThreshold(
    BaseModel
):
    typename__: Literal["DynamicThreshold"] = Field(alias="__typename")
    sensitivity: float
    decision_bounds_type: Optional[DecisionBoundsType] = Field(
        alias="decisionBoundsType"
    )


class GetIncidentGroupIncidentGroupValidatorRelativeVolumeValidatorConfigThresholdFixedThreshold(
    BaseModel
):
    typename__: Literal["FixedThreshold"] = Field(alias="__typename")
    operator: ComparisonOperator
    value: float


class GetIncidentGroupIncidentGroupValidatorRelativeVolumeValidatorReferenceSourceConfig(
    BaseModel
):
    source: "GetIncidentGroupIncidentGroupValidatorRelativeVolumeValidatorReferenceSourceConfigSource"
    window: "GetIncidentGroupIncidentGroupValidatorRelativeVolumeValidatorReferenceSourceConfigWindow"
    history: int
    offset: int
    filter: Optional[JsonFilterExpression]


class GetIncidentGroupIncidentGroupValidatorRelativeVolumeValidatorReferenceSourceConfigSource(
    BaseModel
):
    typename__: Literal[
        "AwsAthenaSource",
        "AwsKinesisSource",
        "AwsRedshiftSource",
        "AwsS3Source",
        "AzureSynapseSource",
        "ClickHouseSource",
        "DatabricksSource",
        "DbtModelRunSource",
        "DbtTestResultSource",
        "DemoSource",
        "GcpBigQuerySource",
        "GcpPubSubLiteSource",
        "GcpPubSubSource",
        "GcpStorageSource",
        "KafkaSource",
        "PostgreSqlSource",
        "SnowflakeSource",
        "Source",
    ] = Field(alias="__typename")
    id: SourceId
    name: str
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")


class GetIncidentGroupIncidentGroupValidatorRelativeVolumeValidatorReferenceSourceConfigWindow(
    BaseModel
):
    typename__: Literal[
        "FileWindow", "FixedBatchWindow", "GlobalWindow", "TumblingWindow", "Window"
    ] = Field(alias="__typename")
    id: WindowId
    name: str
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")


class GetIncidentGroupIncidentGroupValidatorSqlValidator(BaseModel):
    typename__: Literal["SqlValidator"] = Field(alias="__typename")
    id: ValidatorId
    name: str
    has_custom_name: bool = Field(alias="hasCustomName")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    source_config: "GetIncidentGroupIncidentGroupValidatorSqlValidatorSourceConfig" = (
        Field(alias="sourceConfig")
    )
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")
    resource_namespace: str = Field(alias="resourceNamespace")
    config: "GetIncidentGroupIncidentGroupValidatorSqlValidatorConfig"


class GetIncidentGroupIncidentGroupValidatorSqlValidatorSourceConfig(BaseModel):
    source: "GetIncidentGroupIncidentGroupValidatorSqlValidatorSourceConfigSource"
    window: "GetIncidentGroupIncidentGroupValidatorSqlValidatorSourceConfigWindow"
    segmentation: (
        "GetIncidentGroupIncidentGroupValidatorSqlValidatorSourceConfigSegmentation"
    )
    filter: Optional[JsonFilterExpression]


class GetIncidentGroupIncidentGroupValidatorSqlValidatorSourceConfigSource(BaseModel):
    typename__: Literal[
        "AwsAthenaSource",
        "AwsKinesisSource",
        "AwsRedshiftSource",
        "AwsS3Source",
        "AzureSynapseSource",
        "ClickHouseSource",
        "DatabricksSource",
        "DbtModelRunSource",
        "DbtTestResultSource",
        "DemoSource",
        "GcpBigQuerySource",
        "GcpPubSubLiteSource",
        "GcpPubSubSource",
        "GcpStorageSource",
        "KafkaSource",
        "PostgreSqlSource",
        "SnowflakeSource",
        "Source",
    ] = Field(alias="__typename")
    id: SourceId
    name: str
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")


class GetIncidentGroupIncidentGroupValidatorSqlValidatorSourceConfigWindow(BaseModel):
    typename__: Literal[
        "FileWindow", "FixedBatchWindow", "GlobalWindow", "TumblingWindow", "Window"
    ] = Field(alias="__typename")
    id: WindowId
    name: str
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")


class GetIncidentGroupIncidentGroupValidatorSqlValidatorSourceConfigSegmentation(
    BaseModel
):
    typename__: Literal["Segmentation"] = Field(alias="__typename")
    id: SegmentationId
    name: str
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")


class GetIncidentGroupIncidentGroupValidatorSqlValidatorConfig(BaseModel):
    query: str
    threshold: Union[
        "GetIncidentGroupIncidentGroupValidatorSqlValidatorConfigThresholdDynamicThreshold",
        "GetIncidentGroupIncidentGroupValidatorSqlValidatorConfigThresholdFixedThreshold",
    ] = Field(discriminator="typename__")
    initialize_with_backfill: bool = Field(alias="initializeWithBackfill")


class GetIncidentGroupIncidentGroupValidatorSqlValidatorConfigThresholdDynamicThreshold(
    BaseModel
):
    typename__: Literal["DynamicThreshold"] = Field(alias="__typename")
    sensitivity: float
    decision_bounds_type: Optional[DecisionBoundsType] = Field(
        alias="decisionBoundsType"
    )


class GetIncidentGroupIncidentGroupValidatorSqlValidatorConfigThresholdFixedThreshold(
    BaseModel
):
    typename__: Literal["FixedThreshold"] = Field(alias="__typename")
    operator: ComparisonOperator
    value: float


class GetIncidentGroupIncidentGroupValidatorVolumeValidator(BaseModel):
    typename__: Literal["VolumeValidator"] = Field(alias="__typename")
    id: ValidatorId
    name: str
    has_custom_name: bool = Field(alias="hasCustomName")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    source_config: (
        "GetIncidentGroupIncidentGroupValidatorVolumeValidatorSourceConfig"
    ) = Field(alias="sourceConfig")
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")
    resource_namespace: str = Field(alias="resourceNamespace")
    config: "GetIncidentGroupIncidentGroupValidatorVolumeValidatorConfig"


class GetIncidentGroupIncidentGroupValidatorVolumeValidatorSourceConfig(BaseModel):
    source: "GetIncidentGroupIncidentGroupValidatorVolumeValidatorSourceConfigSource"
    window: "GetIncidentGroupIncidentGroupValidatorVolumeValidatorSourceConfigWindow"
    segmentation: (
        "GetIncidentGroupIncidentGroupValidatorVolumeValidatorSourceConfigSegmentation"
    )
    filter: Optional[JsonFilterExpression]


class GetIncidentGroupIncidentGroupValidatorVolumeValidatorSourceConfigSource(
    BaseModel
):
    typename__: Literal[
        "AwsAthenaSource",
        "AwsKinesisSource",
        "AwsRedshiftSource",
        "AwsS3Source",
        "AzureSynapseSource",
        "ClickHouseSource",
        "DatabricksSource",
        "DbtModelRunSource",
        "DbtTestResultSource",
        "DemoSource",
        "GcpBigQuerySource",
        "GcpPubSubLiteSource",
        "GcpPubSubSource",
        "GcpStorageSource",
        "KafkaSource",
        "PostgreSqlSource",
        "SnowflakeSource",
        "Source",
    ] = Field(alias="__typename")
    id: SourceId
    name: str
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")


class GetIncidentGroupIncidentGroupValidatorVolumeValidatorSourceConfigWindow(
    BaseModel
):
    typename__: Literal[
        "FileWindow", "FixedBatchWindow", "GlobalWindow", "TumblingWindow", "Window"
    ] = Field(alias="__typename")
    id: WindowId
    name: str
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")


class GetIncidentGroupIncidentGroupValidatorVolumeValidatorSourceConfigSegmentation(
    BaseModel
):
    typename__: Literal["Segmentation"] = Field(alias="__typename")
    id: SegmentationId
    name: str
    resource_name: str = Field(alias="resourceName")
    namespace_id: str = Field(alias="namespaceId")


class GetIncidentGroupIncidentGroupValidatorVolumeValidatorConfig(BaseModel):
    optional_source_field: Optional[JsonPointer] = Field(alias="optionalSourceField")
    source_fields: List[JsonPointer] = Field(alias="sourceFields")
    volume_metric: VolumeMetric = Field(alias="volumeMetric")
    initialize_with_backfill: bool = Field(alias="initializeWithBackfill")
    threshold: Union[
        "GetIncidentGroupIncidentGroupValidatorVolumeValidatorConfigThresholdDynamicThreshold",
        "GetIncidentGroupIncidentGroupValidatorVolumeValidatorConfigThresholdFixedThreshold",
    ] = Field(discriminator="typename__")


class GetIncidentGroupIncidentGroupValidatorVolumeValidatorConfigThresholdDynamicThreshold(
    BaseModel
):
    typename__: Literal["DynamicThreshold"] = Field(alias="__typename")
    sensitivity: float
    decision_bounds_type: Optional[DecisionBoundsType] = Field(
        alias="decisionBoundsType"
    )


class GetIncidentGroupIncidentGroupValidatorVolumeValidatorConfigThresholdFixedThreshold(
    BaseModel
):
    typename__: Literal["FixedThreshold"] = Field(alias="__typename")
    operator: ComparisonOperator
    value: float


class GetIncidentGroupIncidentGroupSegment(SegmentDetails):
    pass


class GetIncidentGroupIncidentGroupSeverityStats(BaseModel):
    high_count: int = Field(alias="highCount")
    medium_count: int = Field(alias="mediumCount")
    low_count: int = Field(alias="lowCount")
    total_count: int = Field(alias="totalCount")


GetIncidentGroup.model_rebuild()
GetIncidentGroupIncidentGroup.model_rebuild()
GetIncidentGroupIncidentGroupValidatorValidator.model_rebuild()
GetIncidentGroupIncidentGroupValidatorValidatorSourceConfig.model_rebuild()
GetIncidentGroupIncidentGroupValidatorCategoricalDistributionValidator.model_rebuild()
GetIncidentGroupIncidentGroupValidatorCategoricalDistributionValidatorSourceConfig.model_rebuild()
GetIncidentGroupIncidentGroupValidatorCategoricalDistributionValidatorConfig.model_rebuild()
GetIncidentGroupIncidentGroupValidatorCategoricalDistributionValidatorReferenceSourceConfig.model_rebuild()
GetIncidentGroupIncidentGroupValidatorFreshnessValidator.model_rebuild()
GetIncidentGroupIncidentGroupValidatorFreshnessValidatorSourceConfig.model_rebuild()
GetIncidentGroupIncidentGroupValidatorFreshnessValidatorConfig.model_rebuild()
GetIncidentGroupIncidentGroupValidatorNumericAnomalyValidator.model_rebuild()
GetIncidentGroupIncidentGroupValidatorNumericAnomalyValidatorSourceConfig.model_rebuild()
GetIncidentGroupIncidentGroupValidatorNumericAnomalyValidatorConfig.model_rebuild()
GetIncidentGroupIncidentGroupValidatorNumericAnomalyValidatorReferenceSourceConfig.model_rebuild()
GetIncidentGroupIncidentGroupValidatorNumericDistributionValidator.model_rebuild()
GetIncidentGroupIncidentGroupValidatorNumericDistributionValidatorSourceConfig.model_rebuild()
GetIncidentGroupIncidentGroupValidatorNumericDistributionValidatorConfig.model_rebuild()
GetIncidentGroupIncidentGroupValidatorNumericDistributionValidatorReferenceSourceConfig.model_rebuild()
GetIncidentGroupIncidentGroupValidatorNumericValidator.model_rebuild()
GetIncidentGroupIncidentGroupValidatorNumericValidatorSourceConfig.model_rebuild()
GetIncidentGroupIncidentGroupValidatorNumericValidatorConfig.model_rebuild()
GetIncidentGroupIncidentGroupValidatorRelativeTimeValidator.model_rebuild()
GetIncidentGroupIncidentGroupValidatorRelativeTimeValidatorSourceConfig.model_rebuild()
GetIncidentGroupIncidentGroupValidatorRelativeTimeValidatorConfig.model_rebuild()
GetIncidentGroupIncidentGroupValidatorRelativeVolumeValidator.model_rebuild()
GetIncidentGroupIncidentGroupValidatorRelativeVolumeValidatorSourceConfig.model_rebuild()
GetIncidentGroupIncidentGroupValidatorRelativeVolumeValidatorConfig.model_rebuild()
GetIncidentGroupIncidentGroupValidatorRelativeVolumeValidatorReferenceSourceConfig.model_rebuild()
GetIncidentGroupIncidentGroupValidatorSqlValidator.model_rebuild()
GetIncidentGroupIncidentGroupValidatorSqlValidatorSourceConfig.model_rebuild()
GetIncidentGroupIncidentGroupValidatorSqlValidatorConfig.model_rebuild()
GetIncidentGroupIncidentGroupValidatorVolumeValidator.model_rebuild()
GetIncidentGroupIncidentGroupValidatorVolumeValidatorSourceConfig.model_rebuild()
GetIncidentGroupIncidentGroupValidatorVolumeValidatorConfig.model_rebuild()
