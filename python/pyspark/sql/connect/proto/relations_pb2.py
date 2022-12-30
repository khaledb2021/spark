#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spark/connect/relations.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from pyspark.sql.connect.proto import expressions_pb2 as spark_dot_connect_dot_expressions__pb2
from pyspark.sql.connect.proto import types_pb2 as spark_dot_connect_dot_types__pb2
from pyspark.sql.connect.proto import catalog_pb2 as spark_dot_connect_dot_catalog__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1dspark/connect/relations.proto\x12\rspark.connect\x1a\x19google/protobuf/any.proto\x1a\x1fspark/connect/expressions.proto\x1a\x19spark/connect/types.proto\x1a\x1bspark/connect/catalog.proto"\xa4\x11\n\x08Relation\x12\x35\n\x06\x63ommon\x18\x01 \x01(\x0b\x32\x1d.spark.connect.RelationCommonR\x06\x63ommon\x12)\n\x04read\x18\x02 \x01(\x0b\x32\x13.spark.connect.ReadH\x00R\x04read\x12\x32\n\x07project\x18\x03 \x01(\x0b\x32\x16.spark.connect.ProjectH\x00R\x07project\x12/\n\x06\x66ilter\x18\x04 \x01(\x0b\x32\x15.spark.connect.FilterH\x00R\x06\x66ilter\x12)\n\x04join\x18\x05 \x01(\x0b\x32\x13.spark.connect.JoinH\x00R\x04join\x12\x34\n\x06set_op\x18\x06 \x01(\x0b\x32\x1b.spark.connect.SetOperationH\x00R\x05setOp\x12)\n\x04sort\x18\x07 \x01(\x0b\x32\x13.spark.connect.SortH\x00R\x04sort\x12,\n\x05limit\x18\x08 \x01(\x0b\x32\x14.spark.connect.LimitH\x00R\x05limit\x12\x38\n\taggregate\x18\t \x01(\x0b\x32\x18.spark.connect.AggregateH\x00R\taggregate\x12&\n\x03sql\x18\n \x01(\x0b\x32\x12.spark.connect.SQLH\x00R\x03sql\x12\x45\n\x0elocal_relation\x18\x0b \x01(\x0b\x32\x1c.spark.connect.LocalRelationH\x00R\rlocalRelation\x12/\n\x06sample\x18\x0c \x01(\x0b\x32\x15.spark.connect.SampleH\x00R\x06sample\x12/\n\x06offset\x18\r \x01(\x0b\x32\x15.spark.connect.OffsetH\x00R\x06offset\x12>\n\x0b\x64\x65\x64uplicate\x18\x0e \x01(\x0b\x32\x1a.spark.connect.DeduplicateH\x00R\x0b\x64\x65\x64uplicate\x12,\n\x05range\x18\x0f \x01(\x0b\x32\x14.spark.connect.RangeH\x00R\x05range\x12\x45\n\x0esubquery_alias\x18\x10 \x01(\x0b\x32\x1c.spark.connect.SubqueryAliasH\x00R\rsubqueryAlias\x12>\n\x0brepartition\x18\x11 \x01(\x0b\x32\x1a.spark.connect.RepartitionH\x00R\x0brepartition\x12|\n#rename_columns_by_same_length_names\x18\x12 \x01(\x0b\x32-.spark.connect.RenameColumnsBySameLengthNamesH\x00R\x1erenameColumnsBySameLengthNames\x12w\n"rename_columns_by_name_to_name_map\x18\x13 \x01(\x0b\x32+.spark.connect.RenameColumnsByNameToNameMapH\x00R\x1crenameColumnsByNameToNameMap\x12<\n\x0bshow_string\x18\x14 \x01(\x0b\x32\x19.spark.connect.ShowStringH\x00R\nshowString\x12)\n\x04\x64rop\x18\x15 \x01(\x0b\x32\x13.spark.connect.DropH\x00R\x04\x64rop\x12)\n\x04tail\x18\x16 \x01(\x0b\x32\x13.spark.connect.TailH\x00R\x04tail\x12?\n\x0cwith_columns\x18\x17 \x01(\x0b\x32\x1a.spark.connect.WithColumnsH\x00R\x0bwithColumns\x12)\n\x04hint\x18\x18 \x01(\x0b\x32\x13.spark.connect.HintH\x00R\x04hint\x12\x32\n\x07unpivot\x18\x19 \x01(\x0b\x32\x16.spark.connect.UnpivotH\x00R\x07unpivot\x12\x36\n\tto_schema\x18\x1a \x01(\x0b\x32\x17.spark.connect.ToSchemaH\x00R\x08toSchema\x12\x64\n\x19repartition_by_expression\x18\x1b \x01(\x0b\x32&.spark.connect.RepartitionByExpressionH\x00R\x17repartitionByExpression\x12\x30\n\x07\x66ill_na\x18Z \x01(\x0b\x32\x15.spark.connect.NAFillH\x00R\x06\x66illNa\x12\x30\n\x07\x64rop_na\x18[ \x01(\x0b\x32\x15.spark.connect.NADropH\x00R\x06\x64ropNa\x12\x34\n\x07replace\x18\\ \x01(\x0b\x32\x18.spark.connect.NAReplaceH\x00R\x07replace\x12\x36\n\x07summary\x18\x64 \x01(\x0b\x32\x1a.spark.connect.StatSummaryH\x00R\x07summary\x12\x39\n\x08\x63rosstab\x18\x65 \x01(\x0b\x32\x1b.spark.connect.StatCrosstabH\x00R\x08\x63rosstab\x12\x39\n\x08\x64\x65scribe\x18\x66 \x01(\x0b\x32\x1b.spark.connect.StatDescribeH\x00R\x08\x64\x65scribe\x12*\n\x03\x63ov\x18g \x01(\x0b\x32\x16.spark.connect.StatCovH\x00R\x03\x63ov\x12-\n\x04\x63orr\x18h \x01(\x0b\x32\x17.spark.connect.StatCorrH\x00R\x04\x63orr\x12\x33\n\x07\x63\x61talog\x18\xc8\x01 \x01(\x0b\x32\x16.spark.connect.CatalogH\x00R\x07\x63\x61talog\x12\x35\n\textension\x18\xe6\x07 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00R\textension\x12\x33\n\x07unknown\x18\xe7\x07 \x01(\x0b\x32\x16.spark.connect.UnknownH\x00R\x07unknownB\n\n\x08rel_type"\t\n\x07Unknown"1\n\x0eRelationCommon\x12\x1f\n\x0bsource_info\x18\x01 \x01(\tR\nsourceInfo"\x1b\n\x03SQL\x12\x14\n\x05query\x18\x01 \x01(\tR\x05query"\xaa\x03\n\x04Read\x12\x41\n\x0bnamed_table\x18\x01 \x01(\x0b\x32\x1e.spark.connect.Read.NamedTableH\x00R\nnamedTable\x12\x41\n\x0b\x64\x61ta_source\x18\x02 \x01(\x0b\x32\x1e.spark.connect.Read.DataSourceH\x00R\ndataSource\x1a=\n\nNamedTable\x12/\n\x13unparsed_identifier\x18\x01 \x01(\tR\x12unparsedIdentifier\x1a\xcf\x01\n\nDataSource\x12\x16\n\x06\x66ormat\x18\x01 \x01(\tR\x06\x66ormat\x12\x1b\n\x06schema\x18\x02 \x01(\tH\x00R\x06schema\x88\x01\x01\x12\x45\n\x07options\x18\x03 \x03(\x0b\x32+.spark.connect.Read.DataSource.OptionsEntryR\x07options\x1a:\n\x0cOptionsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x42\t\n\x07_schemaB\x0b\n\tread_type"u\n\x07Project\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12;\n\x0b\x65xpressions\x18\x03 \x03(\x0b\x32\x19.spark.connect.ExpressionR\x0b\x65xpressions"p\n\x06\x46ilter\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x37\n\tcondition\x18\x02 \x01(\x0b\x32\x19.spark.connect.ExpressionR\tcondition"\xd7\x03\n\x04Join\x12+\n\x04left\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x04left\x12-\n\x05right\x18\x02 \x01(\x0b\x32\x17.spark.connect.RelationR\x05right\x12@\n\x0ejoin_condition\x18\x03 \x01(\x0b\x32\x19.spark.connect.ExpressionR\rjoinCondition\x12\x39\n\tjoin_type\x18\x04 \x01(\x0e\x32\x1c.spark.connect.Join.JoinTypeR\x08joinType\x12#\n\rusing_columns\x18\x05 \x03(\tR\x0cusingColumns"\xd0\x01\n\x08JoinType\x12\x19\n\x15JOIN_TYPE_UNSPECIFIED\x10\x00\x12\x13\n\x0fJOIN_TYPE_INNER\x10\x01\x12\x18\n\x14JOIN_TYPE_FULL_OUTER\x10\x02\x12\x18\n\x14JOIN_TYPE_LEFT_OUTER\x10\x03\x12\x19\n\x15JOIN_TYPE_RIGHT_OUTER\x10\x04\x12\x17\n\x13JOIN_TYPE_LEFT_ANTI\x10\x05\x12\x17\n\x13JOIN_TYPE_LEFT_SEMI\x10\x06\x12\x13\n\x0fJOIN_TYPE_CROSS\x10\x07"\x8c\x03\n\x0cSetOperation\x12\x36\n\nleft_input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\tleftInput\x12\x38\n\x0bright_input\x18\x02 \x01(\x0b\x32\x17.spark.connect.RelationR\nrightInput\x12\x45\n\x0bset_op_type\x18\x03 \x01(\x0e\x32%.spark.connect.SetOperation.SetOpTypeR\tsetOpType\x12\x1a\n\x06is_all\x18\x04 \x01(\x08H\x00R\x05isAll\x88\x01\x01\x12\x1c\n\x07\x62y_name\x18\x05 \x01(\x08H\x01R\x06\x62yName\x88\x01\x01"r\n\tSetOpType\x12\x1b\n\x17SET_OP_TYPE_UNSPECIFIED\x10\x00\x12\x19\n\x15SET_OP_TYPE_INTERSECT\x10\x01\x12\x15\n\x11SET_OP_TYPE_UNION\x10\x02\x12\x16\n\x12SET_OP_TYPE_EXCEPT\x10\x03\x42\t\n\x07_is_allB\n\n\x08_by_name"L\n\x05Limit\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x14\n\x05limit\x18\x02 \x01(\x05R\x05limit"O\n\x06Offset\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x16\n\x06offset\x18\x02 \x01(\x05R\x06offset"K\n\x04Tail\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x14\n\x05limit\x18\x02 \x01(\x05R\x05limit"\xc6\x04\n\tAggregate\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x41\n\ngroup_type\x18\x02 \x01(\x0e\x32".spark.connect.Aggregate.GroupTypeR\tgroupType\x12L\n\x14grouping_expressions\x18\x03 \x03(\x0b\x32\x19.spark.connect.ExpressionR\x13groupingExpressions\x12N\n\x15\x61ggregate_expressions\x18\x04 \x03(\x0b\x32\x19.spark.connect.ExpressionR\x14\x61ggregateExpressions\x12\x34\n\x05pivot\x18\x05 \x01(\x0b\x32\x1e.spark.connect.Aggregate.PivotR\x05pivot\x1ao\n\x05Pivot\x12+\n\x03\x63ol\x18\x01 \x01(\x0b\x32\x19.spark.connect.ExpressionR\x03\x63ol\x12\x39\n\x06values\x18\x02 \x03(\x0b\x32!.spark.connect.Expression.LiteralR\x06values"\x81\x01\n\tGroupType\x12\x1a\n\x16GROUP_TYPE_UNSPECIFIED\x10\x00\x12\x16\n\x12GROUP_TYPE_GROUPBY\x10\x01\x12\x15\n\x11GROUP_TYPE_ROLLUP\x10\x02\x12\x13\n\x0fGROUP_TYPE_CUBE\x10\x03\x12\x14\n\x10GROUP_TYPE_PIVOT\x10\x04"\xa0\x01\n\x04Sort\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x39\n\x05order\x18\x02 \x03(\x0b\x32#.spark.connect.Expression.SortOrderR\x05order\x12 \n\tis_global\x18\x03 \x01(\x08H\x00R\x08isGlobal\x88\x01\x01\x42\x0c\n\n_is_global"d\n\x04\x44rop\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12-\n\x04\x63ols\x18\x02 \x03(\x0b\x32\x19.spark.connect.ExpressionR\x04\x63ols"\xab\x01\n\x0b\x44\x65\x64uplicate\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12!\n\x0c\x63olumn_names\x18\x02 \x03(\tR\x0b\x63olumnNames\x12\x32\n\x13\x61ll_columns_as_keys\x18\x03 \x01(\x08H\x00R\x10\x61llColumnsAsKeys\x88\x01\x01\x42\x16\n\x14_all_columns_as_keys"\x89\x01\n\rLocalRelation\x12\x12\n\x04\x64\x61ta\x18\x01 \x01(\x0cR\x04\x64\x61ta\x12\x35\n\x08\x64\x61tatype\x18\x02 \x01(\x0b\x32\x17.spark.connect.DataTypeH\x00R\x08\x64\x61tatype\x12#\n\x0c\x64\x61tatype_str\x18\x03 \x01(\tH\x00R\x0b\x64\x61tatypeStrB\x08\n\x06schema"\xa7\x02\n\x06Sample\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x1f\n\x0blower_bound\x18\x02 \x01(\x01R\nlowerBound\x12\x1f\n\x0bupper_bound\x18\x03 \x01(\x01R\nupperBound\x12.\n\x10with_replacement\x18\x04 \x01(\x08H\x00R\x0fwithReplacement\x88\x01\x01\x12\x17\n\x04seed\x18\x05 \x01(\x03H\x01R\x04seed\x88\x01\x01\x12/\n\x11\x66orce_stable_sort\x18\x06 \x01(\x08H\x02R\x0f\x66orceStableSort\x88\x01\x01\x42\x13\n\x11_with_replacementB\x07\n\x05_seedB\x14\n\x12_force_stable_sort"\x91\x01\n\x05Range\x12\x19\n\x05start\x18\x01 \x01(\x03H\x00R\x05start\x88\x01\x01\x12\x10\n\x03\x65nd\x18\x02 \x01(\x03R\x03\x65nd\x12\x12\n\x04step\x18\x03 \x01(\x03R\x04step\x12*\n\x0enum_partitions\x18\x04 \x01(\x05H\x01R\rnumPartitions\x88\x01\x01\x42\x08\n\x06_startB\x11\n\x0f_num_partitions"r\n\rSubqueryAlias\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x14\n\x05\x61lias\x18\x02 \x01(\tR\x05\x61lias\x12\x1c\n\tqualifier\x18\x03 \x03(\tR\tqualifier"\x8e\x01\n\x0bRepartition\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12%\n\x0enum_partitions\x18\x02 \x01(\x05R\rnumPartitions\x12\x1d\n\x07shuffle\x18\x03 \x01(\x08H\x00R\x07shuffle\x88\x01\x01\x42\n\n\x08_shuffle"\x8e\x01\n\nShowString\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x19\n\x08num_rows\x18\x02 \x01(\x05R\x07numRows\x12\x1a\n\x08truncate\x18\x03 \x01(\x05R\x08truncate\x12\x1a\n\x08vertical\x18\x04 \x01(\x08R\x08vertical"\\\n\x0bStatSummary\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x1e\n\nstatistics\x18\x02 \x03(\tR\nstatistics"Q\n\x0cStatDescribe\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x12\n\x04\x63ols\x18\x02 \x03(\tR\x04\x63ols"e\n\x0cStatCrosstab\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x12\n\x04\x63ol1\x18\x02 \x01(\tR\x04\x63ol1\x12\x12\n\x04\x63ol2\x18\x03 \x01(\tR\x04\x63ol2"`\n\x07StatCov\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x12\n\x04\x63ol1\x18\x02 \x01(\tR\x04\x63ol1\x12\x12\n\x04\x63ol2\x18\x03 \x01(\tR\x04\x63ol2"\x89\x01\n\x08StatCorr\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x12\n\x04\x63ol1\x18\x02 \x01(\tR\x04\x63ol1\x12\x12\n\x04\x63ol2\x18\x03 \x01(\tR\x04\x63ol2\x12\x1b\n\x06method\x18\x04 \x01(\tH\x00R\x06method\x88\x01\x01\x42\t\n\x07_method"\x86\x01\n\x06NAFill\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x12\n\x04\x63ols\x18\x02 \x03(\tR\x04\x63ols\x12\x39\n\x06values\x18\x03 \x03(\x0b\x32!.spark.connect.Expression.LiteralR\x06values"\x86\x01\n\x06NADrop\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x12\n\x04\x63ols\x18\x02 \x03(\tR\x04\x63ols\x12\'\n\rmin_non_nulls\x18\x03 \x01(\x05H\x00R\x0bminNonNulls\x88\x01\x01\x42\x10\n\x0e_min_non_nulls"\xa8\x02\n\tNAReplace\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x12\n\x04\x63ols\x18\x02 \x03(\tR\x04\x63ols\x12H\n\x0creplacements\x18\x03 \x03(\x0b\x32$.spark.connect.NAReplace.ReplacementR\x0creplacements\x1a\x8d\x01\n\x0bReplacement\x12>\n\told_value\x18\x01 \x01(\x0b\x32!.spark.connect.Expression.LiteralR\x08oldValue\x12>\n\tnew_value\x18\x02 \x01(\x0b\x32!.spark.connect.Expression.LiteralR\x08newValue"r\n\x1eRenameColumnsBySameLengthNames\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12!\n\x0c\x63olumn_names\x18\x02 \x03(\tR\x0b\x63olumnNames"\x83\x02\n\x1cRenameColumnsByNameToNameMap\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12o\n\x12rename_columns_map\x18\x02 \x03(\x0b\x32\x41.spark.connect.RenameColumnsByNameToNameMap.RenameColumnsMapEntryR\x10renameColumnsMap\x1a\x43\n\x15RenameColumnsMapEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01"\x83\x01\n\x0bWithColumns\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x45\n\x0ename_expr_list\x18\x02 \x03(\x0b\x32\x1f.spark.connect.Expression.AliasR\x0cnameExprList"\x8c\x01\n\x04Hint\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x41\n\nparameters\x18\x03 \x03(\x0b\x32!.spark.connect.Expression.LiteralR\nparameters"\xf6\x01\n\x07Unpivot\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12+\n\x03ids\x18\x02 \x03(\x0b\x32\x19.spark.connect.ExpressionR\x03ids\x12\x31\n\x06values\x18\x03 \x03(\x0b\x32\x19.spark.connect.ExpressionR\x06values\x12\x30\n\x14variable_column_name\x18\x04 \x01(\tR\x12variableColumnName\x12*\n\x11value_column_name\x18\x05 \x01(\tR\x0fvalueColumnName"j\n\x08ToSchema\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12/\n\x06schema\x18\x02 \x01(\x0b\x32\x17.spark.connect.DataTypeR\x06schema"\xcb\x01\n\x17RepartitionByExpression\x12-\n\x05input\x18\x01 \x01(\x0b\x32\x17.spark.connect.RelationR\x05input\x12\x42\n\x0fpartition_exprs\x18\x02 \x03(\x0b\x32\x19.spark.connect.ExpressionR\x0epartitionExprs\x12*\n\x0enum_partitions\x18\x03 \x01(\x05H\x00R\rnumPartitions\x88\x01\x01\x42\x11\n\x0f_num_partitionsB"\n\x1eorg.apache.spark.connect.protoP\x01\x62\x06proto3'
)


_RELATION = DESCRIPTOR.message_types_by_name["Relation"]
_UNKNOWN = DESCRIPTOR.message_types_by_name["Unknown"]
_RELATIONCOMMON = DESCRIPTOR.message_types_by_name["RelationCommon"]
_SQL = DESCRIPTOR.message_types_by_name["SQL"]
_READ = DESCRIPTOR.message_types_by_name["Read"]
_READ_NAMEDTABLE = _READ.nested_types_by_name["NamedTable"]
_READ_DATASOURCE = _READ.nested_types_by_name["DataSource"]
_READ_DATASOURCE_OPTIONSENTRY = _READ_DATASOURCE.nested_types_by_name["OptionsEntry"]
_PROJECT = DESCRIPTOR.message_types_by_name["Project"]
_FILTER = DESCRIPTOR.message_types_by_name["Filter"]
_JOIN = DESCRIPTOR.message_types_by_name["Join"]
_SETOPERATION = DESCRIPTOR.message_types_by_name["SetOperation"]
_LIMIT = DESCRIPTOR.message_types_by_name["Limit"]
_OFFSET = DESCRIPTOR.message_types_by_name["Offset"]
_TAIL = DESCRIPTOR.message_types_by_name["Tail"]
_AGGREGATE = DESCRIPTOR.message_types_by_name["Aggregate"]
_AGGREGATE_PIVOT = _AGGREGATE.nested_types_by_name["Pivot"]
_SORT = DESCRIPTOR.message_types_by_name["Sort"]
_DROP = DESCRIPTOR.message_types_by_name["Drop"]
_DEDUPLICATE = DESCRIPTOR.message_types_by_name["Deduplicate"]
_LOCALRELATION = DESCRIPTOR.message_types_by_name["LocalRelation"]
_SAMPLE = DESCRIPTOR.message_types_by_name["Sample"]
_RANGE = DESCRIPTOR.message_types_by_name["Range"]
_SUBQUERYALIAS = DESCRIPTOR.message_types_by_name["SubqueryAlias"]
_REPARTITION = DESCRIPTOR.message_types_by_name["Repartition"]
_SHOWSTRING = DESCRIPTOR.message_types_by_name["ShowString"]
_STATSUMMARY = DESCRIPTOR.message_types_by_name["StatSummary"]
_STATDESCRIBE = DESCRIPTOR.message_types_by_name["StatDescribe"]
_STATCROSSTAB = DESCRIPTOR.message_types_by_name["StatCrosstab"]
_STATCOV = DESCRIPTOR.message_types_by_name["StatCov"]
_STATCORR = DESCRIPTOR.message_types_by_name["StatCorr"]
_NAFILL = DESCRIPTOR.message_types_by_name["NAFill"]
_NADROP = DESCRIPTOR.message_types_by_name["NADrop"]
_NAREPLACE = DESCRIPTOR.message_types_by_name["NAReplace"]
_NAREPLACE_REPLACEMENT = _NAREPLACE.nested_types_by_name["Replacement"]
_RENAMECOLUMNSBYSAMELENGTHNAMES = DESCRIPTOR.message_types_by_name["RenameColumnsBySameLengthNames"]
_RENAMECOLUMNSBYNAMETONAMEMAP = DESCRIPTOR.message_types_by_name["RenameColumnsByNameToNameMap"]
_RENAMECOLUMNSBYNAMETONAMEMAP_RENAMECOLUMNSMAPENTRY = (
    _RENAMECOLUMNSBYNAMETONAMEMAP.nested_types_by_name["RenameColumnsMapEntry"]
)
_WITHCOLUMNS = DESCRIPTOR.message_types_by_name["WithColumns"]
_HINT = DESCRIPTOR.message_types_by_name["Hint"]
_UNPIVOT = DESCRIPTOR.message_types_by_name["Unpivot"]
_TOSCHEMA = DESCRIPTOR.message_types_by_name["ToSchema"]
_REPARTITIONBYEXPRESSION = DESCRIPTOR.message_types_by_name["RepartitionByExpression"]
_JOIN_JOINTYPE = _JOIN.enum_types_by_name["JoinType"]
_SETOPERATION_SETOPTYPE = _SETOPERATION.enum_types_by_name["SetOpType"]
_AGGREGATE_GROUPTYPE = _AGGREGATE.enum_types_by_name["GroupType"]
Relation = _reflection.GeneratedProtocolMessageType(
    "Relation",
    (_message.Message,),
    {
        "DESCRIPTOR": _RELATION,
        "__module__": "spark.connect.relations_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.Relation)
    },
)
_sym_db.RegisterMessage(Relation)

Unknown = _reflection.GeneratedProtocolMessageType(
    "Unknown",
    (_message.Message,),
    {
        "DESCRIPTOR": _UNKNOWN,
        "__module__": "spark.connect.relations_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.Unknown)
    },
)
_sym_db.RegisterMessage(Unknown)

RelationCommon = _reflection.GeneratedProtocolMessageType(
    "RelationCommon",
    (_message.Message,),
    {
        "DESCRIPTOR": _RELATIONCOMMON,
        "__module__": "spark.connect.relations_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.RelationCommon)
    },
)
_sym_db.RegisterMessage(RelationCommon)

SQL = _reflection.GeneratedProtocolMessageType(
    "SQL",
    (_message.Message,),
    {
        "DESCRIPTOR": _SQL,
        "__module__": "spark.connect.relations_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.SQL)
    },
)
_sym_db.RegisterMessage(SQL)

Read = _reflection.GeneratedProtocolMessageType(
    "Read",
    (_message.Message,),
    {
        "NamedTable": _reflection.GeneratedProtocolMessageType(
            "NamedTable",
            (_message.Message,),
            {
                "DESCRIPTOR": _READ_NAMEDTABLE,
                "__module__": "spark.connect.relations_pb2"
                # @@protoc_insertion_point(class_scope:spark.connect.Read.NamedTable)
            },
        ),
        "DataSource": _reflection.GeneratedProtocolMessageType(
            "DataSource",
            (_message.Message,),
            {
                "OptionsEntry": _reflection.GeneratedProtocolMessageType(
                    "OptionsEntry",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _READ_DATASOURCE_OPTIONSENTRY,
                        "__module__": "spark.connect.relations_pb2"
                        # @@protoc_insertion_point(class_scope:spark.connect.Read.DataSource.OptionsEntry)
                    },
                ),
                "DESCRIPTOR": _READ_DATASOURCE,
                "__module__": "spark.connect.relations_pb2"
                # @@protoc_insertion_point(class_scope:spark.connect.Read.DataSource)
            },
        ),
        "DESCRIPTOR": _READ,
        "__module__": "spark.connect.relations_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.Read)
    },
)
_sym_db.RegisterMessage(Read)
_sym_db.RegisterMessage(Read.NamedTable)
_sym_db.RegisterMessage(Read.DataSource)
_sym_db.RegisterMessage(Read.DataSource.OptionsEntry)

Project = _reflection.GeneratedProtocolMessageType(
    "Project",
    (_message.Message,),
    {
        "DESCRIPTOR": _PROJECT,
        "__module__": "spark.connect.relations_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.Project)
    },
)
_sym_db.RegisterMessage(Project)

Filter = _reflection.GeneratedProtocolMessageType(
    "Filter",
    (_message.Message,),
    {
        "DESCRIPTOR": _FILTER,
        "__module__": "spark.connect.relations_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.Filter)
    },
)
_sym_db.RegisterMessage(Filter)

Join = _reflection.GeneratedProtocolMessageType(
    "Join",
    (_message.Message,),
    {
        "DESCRIPTOR": _JOIN,
        "__module__": "spark.connect.relations_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.Join)
    },
)
_sym_db.RegisterMessage(Join)

SetOperation = _reflection.GeneratedProtocolMessageType(
    "SetOperation",
    (_message.Message,),
    {
        "DESCRIPTOR": _SETOPERATION,
        "__module__": "spark.connect.relations_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.SetOperation)
    },
)
_sym_db.RegisterMessage(SetOperation)

Limit = _reflection.GeneratedProtocolMessageType(
    "Limit",
    (_message.Message,),
    {
        "DESCRIPTOR": _LIMIT,
        "__module__": "spark.connect.relations_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.Limit)
    },
)
_sym_db.RegisterMessage(Limit)

Offset = _reflection.GeneratedProtocolMessageType(
    "Offset",
    (_message.Message,),
    {
        "DESCRIPTOR": _OFFSET,
        "__module__": "spark.connect.relations_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.Offset)
    },
)
_sym_db.RegisterMessage(Offset)

Tail = _reflection.GeneratedProtocolMessageType(
    "Tail",
    (_message.Message,),
    {
        "DESCRIPTOR": _TAIL,
        "__module__": "spark.connect.relations_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.Tail)
    },
)
_sym_db.RegisterMessage(Tail)

Aggregate = _reflection.GeneratedProtocolMessageType(
    "Aggregate",
    (_message.Message,),
    {
        "Pivot": _reflection.GeneratedProtocolMessageType(
            "Pivot",
            (_message.Message,),
            {
                "DESCRIPTOR": _AGGREGATE_PIVOT,
                "__module__": "spark.connect.relations_pb2"
                # @@protoc_insertion_point(class_scope:spark.connect.Aggregate.Pivot)
            },
        ),
        "DESCRIPTOR": _AGGREGATE,
        "__module__": "spark.connect.relations_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.Aggregate)
    },
)
_sym_db.RegisterMessage(Aggregate)
_sym_db.RegisterMessage(Aggregate.Pivot)

Sort = _reflection.GeneratedProtocolMessageType(
    "Sort",
    (_message.Message,),
    {
        "DESCRIPTOR": _SORT,
        "__module__": "spark.connect.relations_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.Sort)
    },
)
_sym_db.RegisterMessage(Sort)

Drop = _reflection.GeneratedProtocolMessageType(
    "Drop",
    (_message.Message,),
    {
        "DESCRIPTOR": _DROP,
        "__module__": "spark.connect.relations_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.Drop)
    },
)
_sym_db.RegisterMessage(Drop)

Deduplicate = _reflection.GeneratedProtocolMessageType(
    "Deduplicate",
    (_message.Message,),
    {
        "DESCRIPTOR": _DEDUPLICATE,
        "__module__": "spark.connect.relations_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.Deduplicate)
    },
)
_sym_db.RegisterMessage(Deduplicate)

LocalRelation = _reflection.GeneratedProtocolMessageType(
    "LocalRelation",
    (_message.Message,),
    {
        "DESCRIPTOR": _LOCALRELATION,
        "__module__": "spark.connect.relations_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.LocalRelation)
    },
)
_sym_db.RegisterMessage(LocalRelation)

Sample = _reflection.GeneratedProtocolMessageType(
    "Sample",
    (_message.Message,),
    {
        "DESCRIPTOR": _SAMPLE,
        "__module__": "spark.connect.relations_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.Sample)
    },
)
_sym_db.RegisterMessage(Sample)

Range = _reflection.GeneratedProtocolMessageType(
    "Range",
    (_message.Message,),
    {
        "DESCRIPTOR": _RANGE,
        "__module__": "spark.connect.relations_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.Range)
    },
)
_sym_db.RegisterMessage(Range)

SubqueryAlias = _reflection.GeneratedProtocolMessageType(
    "SubqueryAlias",
    (_message.Message,),
    {
        "DESCRIPTOR": _SUBQUERYALIAS,
        "__module__": "spark.connect.relations_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.SubqueryAlias)
    },
)
_sym_db.RegisterMessage(SubqueryAlias)

Repartition = _reflection.GeneratedProtocolMessageType(
    "Repartition",
    (_message.Message,),
    {
        "DESCRIPTOR": _REPARTITION,
        "__module__": "spark.connect.relations_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.Repartition)
    },
)
_sym_db.RegisterMessage(Repartition)

ShowString = _reflection.GeneratedProtocolMessageType(
    "ShowString",
    (_message.Message,),
    {
        "DESCRIPTOR": _SHOWSTRING,
        "__module__": "spark.connect.relations_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.ShowString)
    },
)
_sym_db.RegisterMessage(ShowString)

StatSummary = _reflection.GeneratedProtocolMessageType(
    "StatSummary",
    (_message.Message,),
    {
        "DESCRIPTOR": _STATSUMMARY,
        "__module__": "spark.connect.relations_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.StatSummary)
    },
)
_sym_db.RegisterMessage(StatSummary)

StatDescribe = _reflection.GeneratedProtocolMessageType(
    "StatDescribe",
    (_message.Message,),
    {
        "DESCRIPTOR": _STATDESCRIBE,
        "__module__": "spark.connect.relations_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.StatDescribe)
    },
)
_sym_db.RegisterMessage(StatDescribe)

StatCrosstab = _reflection.GeneratedProtocolMessageType(
    "StatCrosstab",
    (_message.Message,),
    {
        "DESCRIPTOR": _STATCROSSTAB,
        "__module__": "spark.connect.relations_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.StatCrosstab)
    },
)
_sym_db.RegisterMessage(StatCrosstab)

StatCov = _reflection.GeneratedProtocolMessageType(
    "StatCov",
    (_message.Message,),
    {
        "DESCRIPTOR": _STATCOV,
        "__module__": "spark.connect.relations_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.StatCov)
    },
)
_sym_db.RegisterMessage(StatCov)

StatCorr = _reflection.GeneratedProtocolMessageType(
    "StatCorr",
    (_message.Message,),
    {
        "DESCRIPTOR": _STATCORR,
        "__module__": "spark.connect.relations_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.StatCorr)
    },
)
_sym_db.RegisterMessage(StatCorr)

NAFill = _reflection.GeneratedProtocolMessageType(
    "NAFill",
    (_message.Message,),
    {
        "DESCRIPTOR": _NAFILL,
        "__module__": "spark.connect.relations_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.NAFill)
    },
)
_sym_db.RegisterMessage(NAFill)

NADrop = _reflection.GeneratedProtocolMessageType(
    "NADrop",
    (_message.Message,),
    {
        "DESCRIPTOR": _NADROP,
        "__module__": "spark.connect.relations_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.NADrop)
    },
)
_sym_db.RegisterMessage(NADrop)

NAReplace = _reflection.GeneratedProtocolMessageType(
    "NAReplace",
    (_message.Message,),
    {
        "Replacement": _reflection.GeneratedProtocolMessageType(
            "Replacement",
            (_message.Message,),
            {
                "DESCRIPTOR": _NAREPLACE_REPLACEMENT,
                "__module__": "spark.connect.relations_pb2"
                # @@protoc_insertion_point(class_scope:spark.connect.NAReplace.Replacement)
            },
        ),
        "DESCRIPTOR": _NAREPLACE,
        "__module__": "spark.connect.relations_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.NAReplace)
    },
)
_sym_db.RegisterMessage(NAReplace)
_sym_db.RegisterMessage(NAReplace.Replacement)

RenameColumnsBySameLengthNames = _reflection.GeneratedProtocolMessageType(
    "RenameColumnsBySameLengthNames",
    (_message.Message,),
    {
        "DESCRIPTOR": _RENAMECOLUMNSBYSAMELENGTHNAMES,
        "__module__": "spark.connect.relations_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.RenameColumnsBySameLengthNames)
    },
)
_sym_db.RegisterMessage(RenameColumnsBySameLengthNames)

RenameColumnsByNameToNameMap = _reflection.GeneratedProtocolMessageType(
    "RenameColumnsByNameToNameMap",
    (_message.Message,),
    {
        "RenameColumnsMapEntry": _reflection.GeneratedProtocolMessageType(
            "RenameColumnsMapEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _RENAMECOLUMNSBYNAMETONAMEMAP_RENAMECOLUMNSMAPENTRY,
                "__module__": "spark.connect.relations_pb2"
                # @@protoc_insertion_point(class_scope:spark.connect.RenameColumnsByNameToNameMap.RenameColumnsMapEntry)
            },
        ),
        "DESCRIPTOR": _RENAMECOLUMNSBYNAMETONAMEMAP,
        "__module__": "spark.connect.relations_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.RenameColumnsByNameToNameMap)
    },
)
_sym_db.RegisterMessage(RenameColumnsByNameToNameMap)
_sym_db.RegisterMessage(RenameColumnsByNameToNameMap.RenameColumnsMapEntry)

WithColumns = _reflection.GeneratedProtocolMessageType(
    "WithColumns",
    (_message.Message,),
    {
        "DESCRIPTOR": _WITHCOLUMNS,
        "__module__": "spark.connect.relations_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.WithColumns)
    },
)
_sym_db.RegisterMessage(WithColumns)

Hint = _reflection.GeneratedProtocolMessageType(
    "Hint",
    (_message.Message,),
    {
        "DESCRIPTOR": _HINT,
        "__module__": "spark.connect.relations_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.Hint)
    },
)
_sym_db.RegisterMessage(Hint)

Unpivot = _reflection.GeneratedProtocolMessageType(
    "Unpivot",
    (_message.Message,),
    {
        "DESCRIPTOR": _UNPIVOT,
        "__module__": "spark.connect.relations_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.Unpivot)
    },
)
_sym_db.RegisterMessage(Unpivot)

ToSchema = _reflection.GeneratedProtocolMessageType(
    "ToSchema",
    (_message.Message,),
    {
        "DESCRIPTOR": _TOSCHEMA,
        "__module__": "spark.connect.relations_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.ToSchema)
    },
)
_sym_db.RegisterMessage(ToSchema)

RepartitionByExpression = _reflection.GeneratedProtocolMessageType(
    "RepartitionByExpression",
    (_message.Message,),
    {
        "DESCRIPTOR": _REPARTITIONBYEXPRESSION,
        "__module__": "spark.connect.relations_pb2"
        # @@protoc_insertion_point(class_scope:spark.connect.RepartitionByExpression)
    },
)
_sym_db.RegisterMessage(RepartitionByExpression)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\036org.apache.spark.connect.protoP\001"
    _READ_DATASOURCE_OPTIONSENTRY._options = None
    _READ_DATASOURCE_OPTIONSENTRY._serialized_options = b"8\001"
    _RENAMECOLUMNSBYNAMETONAMEMAP_RENAMECOLUMNSMAPENTRY._options = None
    _RENAMECOLUMNSBYNAMETONAMEMAP_RENAMECOLUMNSMAPENTRY._serialized_options = b"8\001"
    _RELATION._serialized_start = 165
    _RELATION._serialized_end = 2377
    _UNKNOWN._serialized_start = 2379
    _UNKNOWN._serialized_end = 2388
    _RELATIONCOMMON._serialized_start = 2390
    _RELATIONCOMMON._serialized_end = 2439
    _SQL._serialized_start = 2441
    _SQL._serialized_end = 2468
    _READ._serialized_start = 2471
    _READ._serialized_end = 2897
    _READ_NAMEDTABLE._serialized_start = 2613
    _READ_NAMEDTABLE._serialized_end = 2674
    _READ_DATASOURCE._serialized_start = 2677
    _READ_DATASOURCE._serialized_end = 2884
    _READ_DATASOURCE_OPTIONSENTRY._serialized_start = 2815
    _READ_DATASOURCE_OPTIONSENTRY._serialized_end = 2873
    _PROJECT._serialized_start = 2899
    _PROJECT._serialized_end = 3016
    _FILTER._serialized_start = 3018
    _FILTER._serialized_end = 3130
    _JOIN._serialized_start = 3133
    _JOIN._serialized_end = 3604
    _JOIN_JOINTYPE._serialized_start = 3396
    _JOIN_JOINTYPE._serialized_end = 3604
    _SETOPERATION._serialized_start = 3607
    _SETOPERATION._serialized_end = 4003
    _SETOPERATION_SETOPTYPE._serialized_start = 3866
    _SETOPERATION_SETOPTYPE._serialized_end = 3980
    _LIMIT._serialized_start = 4005
    _LIMIT._serialized_end = 4081
    _OFFSET._serialized_start = 4083
    _OFFSET._serialized_end = 4162
    _TAIL._serialized_start = 4164
    _TAIL._serialized_end = 4239
    _AGGREGATE._serialized_start = 4242
    _AGGREGATE._serialized_end = 4824
    _AGGREGATE_PIVOT._serialized_start = 4581
    _AGGREGATE_PIVOT._serialized_end = 4692
    _AGGREGATE_GROUPTYPE._serialized_start = 4695
    _AGGREGATE_GROUPTYPE._serialized_end = 4824
    _SORT._serialized_start = 4827
    _SORT._serialized_end = 4987
    _DROP._serialized_start = 4989
    _DROP._serialized_end = 5089
    _DEDUPLICATE._serialized_start = 5092
    _DEDUPLICATE._serialized_end = 5263
    _LOCALRELATION._serialized_start = 5266
    _LOCALRELATION._serialized_end = 5403
    _SAMPLE._serialized_start = 5406
    _SAMPLE._serialized_end = 5701
    _RANGE._serialized_start = 5704
    _RANGE._serialized_end = 5849
    _SUBQUERYALIAS._serialized_start = 5851
    _SUBQUERYALIAS._serialized_end = 5965
    _REPARTITION._serialized_start = 5968
    _REPARTITION._serialized_end = 6110
    _SHOWSTRING._serialized_start = 6113
    _SHOWSTRING._serialized_end = 6255
    _STATSUMMARY._serialized_start = 6257
    _STATSUMMARY._serialized_end = 6349
    _STATDESCRIBE._serialized_start = 6351
    _STATDESCRIBE._serialized_end = 6432
    _STATCROSSTAB._serialized_start = 6434
    _STATCROSSTAB._serialized_end = 6535
    _STATCOV._serialized_start = 6537
    _STATCOV._serialized_end = 6633
    _STATCORR._serialized_start = 6636
    _STATCORR._serialized_end = 6773
    _NAFILL._serialized_start = 6776
    _NAFILL._serialized_end = 6910
    _NADROP._serialized_start = 6913
    _NADROP._serialized_end = 7047
    _NAREPLACE._serialized_start = 7050
    _NAREPLACE._serialized_end = 7346
    _NAREPLACE_REPLACEMENT._serialized_start = 7205
    _NAREPLACE_REPLACEMENT._serialized_end = 7346
    _RENAMECOLUMNSBYSAMELENGTHNAMES._serialized_start = 7348
    _RENAMECOLUMNSBYSAMELENGTHNAMES._serialized_end = 7462
    _RENAMECOLUMNSBYNAMETONAMEMAP._serialized_start = 7465
    _RENAMECOLUMNSBYNAMETONAMEMAP._serialized_end = 7724
    _RENAMECOLUMNSBYNAMETONAMEMAP_RENAMECOLUMNSMAPENTRY._serialized_start = 7657
    _RENAMECOLUMNSBYNAMETONAMEMAP_RENAMECOLUMNSMAPENTRY._serialized_end = 7724
    _WITHCOLUMNS._serialized_start = 7727
    _WITHCOLUMNS._serialized_end = 7858
    _HINT._serialized_start = 7861
    _HINT._serialized_end = 8001
    _UNPIVOT._serialized_start = 8004
    _UNPIVOT._serialized_end = 8250
    _TOSCHEMA._serialized_start = 8252
    _TOSCHEMA._serialized_end = 8358
    _REPARTITIONBYEXPRESSION._serialized_start = 8361
    _REPARTITIONBYEXPRESSION._serialized_end = 8564
# @@protoc_insertion_point(module_scope)
