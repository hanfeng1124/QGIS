# The following has been generated automatically from src/gui/processing/qgsprocessingtoolboxmodel.h
# monkey patching scoped based enum
QgsProcessingToolboxModelNode.NodeProvider = QgsProcessingToolboxModelNode.NodeType.Provider
QgsProcessingToolboxModelNode.NodeType.NodeProvider = QgsProcessingToolboxModelNode.NodeType.Provider
QgsProcessingToolboxModelNode.NodeProvider.is_monkey_patched = True
QgsProcessingToolboxModelNode.NodeProvider.__doc__ = "Provider node"
QgsProcessingToolboxModelNode.NodeGroup = QgsProcessingToolboxModelNode.NodeType.Group
QgsProcessingToolboxModelNode.NodeType.NodeGroup = QgsProcessingToolboxModelNode.NodeType.Group
QgsProcessingToolboxModelNode.NodeGroup.is_monkey_patched = True
QgsProcessingToolboxModelNode.NodeGroup.__doc__ = "Group node"
QgsProcessingToolboxModelNode.NodeAlgorithm = QgsProcessingToolboxModelNode.NodeType.Algorithm
QgsProcessingToolboxModelNode.NodeType.NodeAlgorithm = QgsProcessingToolboxModelNode.NodeType.Algorithm
QgsProcessingToolboxModelNode.NodeAlgorithm.is_monkey_patched = True
QgsProcessingToolboxModelNode.NodeAlgorithm.__doc__ = "Algorithm node"
QgsProcessingToolboxModelNode.NodeRecent = QgsProcessingToolboxModelNode.NodeType.Recent
QgsProcessingToolboxModelNode.NodeType.NodeRecent = QgsProcessingToolboxModelNode.NodeType.Recent
QgsProcessingToolboxModelNode.NodeRecent.is_monkey_patched = True
QgsProcessingToolboxModelNode.NodeRecent.__doc__ = "Recent algorithms node"
QgsProcessingToolboxModelNode.NodeType.__doc__ = "Enumeration of possible model node types\n\n" + '* ``NodeProvider``: ' + QgsProcessingToolboxModelNode.NodeType.Provider.__doc__ + '\n' + '* ``NodeGroup``: ' + QgsProcessingToolboxModelNode.NodeType.Group.__doc__ + '\n' + '* ``NodeAlgorithm``: ' + QgsProcessingToolboxModelNode.NodeType.Algorithm.__doc__ + '\n' + '* ``NodeRecent``: ' + QgsProcessingToolboxModelNode.NodeType.Recent.__doc__
# --
QgsProcessingToolboxModelNode.NodeType.baseClass = QgsProcessingToolboxModelNode
QgsProcessingToolboxModel.Roles = QgsProcessingToolboxModel.CustomRole
# monkey patching scoped based enum
QgsProcessingToolboxModel.RoleNodeType = QgsProcessingToolboxModel.CustomRole.NodeType
QgsProcessingToolboxModel.Roles.RoleNodeType = QgsProcessingToolboxModel.CustomRole.NodeType
QgsProcessingToolboxModel.RoleNodeType.is_monkey_patched = True
QgsProcessingToolboxModel.RoleNodeType.__doc__ = "Corresponds to the node's type"
QgsProcessingToolboxModel.RoleAlgorithmFlags = QgsProcessingToolboxModel.CustomRole.AlgorithmFlags
QgsProcessingToolboxModel.Roles.RoleAlgorithmFlags = QgsProcessingToolboxModel.CustomRole.AlgorithmFlags
QgsProcessingToolboxModel.RoleAlgorithmFlags.is_monkey_patched = True
QgsProcessingToolboxModel.RoleAlgorithmFlags.__doc__ = "Returns the node's algorithm flags, for algorithm nodes"
QgsProcessingToolboxModel.RoleAlgorithmId = QgsProcessingToolboxModel.CustomRole.AlgorithmId
QgsProcessingToolboxModel.Roles.RoleAlgorithmId = QgsProcessingToolboxModel.CustomRole.AlgorithmId
QgsProcessingToolboxModel.RoleAlgorithmId.is_monkey_patched = True
QgsProcessingToolboxModel.RoleAlgorithmId.__doc__ = "Algorithm ID, for algorithm nodes"
QgsProcessingToolboxModel.RoleAlgorithmName = QgsProcessingToolboxModel.CustomRole.AlgorithmName
QgsProcessingToolboxModel.Roles.RoleAlgorithmName = QgsProcessingToolboxModel.CustomRole.AlgorithmName
QgsProcessingToolboxModel.RoleAlgorithmName.is_monkey_patched = True
QgsProcessingToolboxModel.RoleAlgorithmName.__doc__ = "Untranslated algorithm name, for algorithm nodes"
QgsProcessingToolboxModel.RoleAlgorithmShortDescription = QgsProcessingToolboxModel.CustomRole.AlgorithmShortDescription
QgsProcessingToolboxModel.Roles.RoleAlgorithmShortDescription = QgsProcessingToolboxModel.CustomRole.AlgorithmShortDescription
QgsProcessingToolboxModel.RoleAlgorithmShortDescription.is_monkey_patched = True
QgsProcessingToolboxModel.RoleAlgorithmShortDescription.__doc__ = "Short algorithm description, for algorithm nodes"
QgsProcessingToolboxModel.RoleAlgorithmTags = QgsProcessingToolboxModel.CustomRole.AlgorithmTags
QgsProcessingToolboxModel.Roles.RoleAlgorithmTags = QgsProcessingToolboxModel.CustomRole.AlgorithmTags
QgsProcessingToolboxModel.RoleAlgorithmTags.is_monkey_patched = True
QgsProcessingToolboxModel.RoleAlgorithmTags.__doc__ = "List of algorithm tags, for algorithm nodes"
QgsProcessingToolboxModel.RoleProviderFlags = QgsProcessingToolboxModel.CustomRole.ProviderFlags
QgsProcessingToolboxModel.Roles.RoleProviderFlags = QgsProcessingToolboxModel.CustomRole.ProviderFlags
QgsProcessingToolboxModel.RoleProviderFlags.is_monkey_patched = True
QgsProcessingToolboxModel.RoleProviderFlags.__doc__ = "Returns the node's provider flags"
QgsProcessingToolboxModel.CustomRole.__doc__ = "Custom model roles.\n\n.. note::\n\n   Prior to QGIS 3.36 this was available as QgsProcessingToolboxModel.Roles\n\n.. versionadded:: 3.36\n\n" + '* ``RoleNodeType``: ' + QgsProcessingToolboxModel.CustomRole.NodeType.__doc__ + '\n' + '* ``RoleAlgorithmFlags``: ' + QgsProcessingToolboxModel.CustomRole.AlgorithmFlags.__doc__ + '\n' + '* ``RoleAlgorithmId``: ' + QgsProcessingToolboxModel.CustomRole.AlgorithmId.__doc__ + '\n' + '* ``RoleAlgorithmName``: ' + QgsProcessingToolboxModel.CustomRole.AlgorithmName.__doc__ + '\n' + '* ``RoleAlgorithmShortDescription``: ' + QgsProcessingToolboxModel.CustomRole.AlgorithmShortDescription.__doc__ + '\n' + '* ``RoleAlgorithmTags``: ' + QgsProcessingToolboxModel.CustomRole.AlgorithmTags.__doc__ + '\n' + '* ``RoleProviderFlags``: ' + QgsProcessingToolboxModel.CustomRole.ProviderFlags.__doc__
# --
QgsProcessingToolboxModel.CustomRole.baseClass = QgsProcessingToolboxModel
# monkey patching scoped based enum
QgsProcessingToolboxProxyModel.FilterToolbox = QgsProcessingToolboxProxyModel.Filter.Toolbox
QgsProcessingToolboxProxyModel.Filter.FilterToolbox = QgsProcessingToolboxProxyModel.Filter.Toolbox
QgsProcessingToolboxProxyModel.FilterToolbox.is_monkey_patched = True
QgsProcessingToolboxProxyModel.FilterToolbox.__doc__ = "Filters out any algorithms and content which should not be shown in the toolbox"
QgsProcessingToolboxProxyModel.FilterModeler = QgsProcessingToolboxProxyModel.Filter.Modeler
QgsProcessingToolboxProxyModel.Filter.FilterModeler = QgsProcessingToolboxProxyModel.Filter.Modeler
QgsProcessingToolboxProxyModel.FilterModeler.is_monkey_patched = True
QgsProcessingToolboxProxyModel.FilterModeler.__doc__ = "Filters out any algorithms and content which should not be shown in the modeler"
QgsProcessingToolboxProxyModel.FilterInPlace = QgsProcessingToolboxProxyModel.Filter.InPlace
QgsProcessingToolboxProxyModel.Filter.FilterInPlace = QgsProcessingToolboxProxyModel.Filter.InPlace
QgsProcessingToolboxProxyModel.FilterInPlace.is_monkey_patched = True
QgsProcessingToolboxProxyModel.FilterInPlace.__doc__ = "Only show algorithms which support in-place edits"
QgsProcessingToolboxProxyModel.FilterShowKnownIssues = QgsProcessingToolboxProxyModel.Filter.ShowKnownIssues
QgsProcessingToolboxProxyModel.Filter.FilterShowKnownIssues = QgsProcessingToolboxProxyModel.Filter.ShowKnownIssues
QgsProcessingToolboxProxyModel.FilterShowKnownIssues.is_monkey_patched = True
QgsProcessingToolboxProxyModel.FilterShowKnownIssues.__doc__ = "Show algorithms with known issues (hidden by default)"
QgsProcessingToolboxProxyModel.Filter.__doc__ = "Available filter flags for filtering the model\n\n" + '* ``FilterToolbox``: ' + QgsProcessingToolboxProxyModel.Filter.Toolbox.__doc__ + '\n' + '* ``FilterModeler``: ' + QgsProcessingToolboxProxyModel.Filter.Modeler.__doc__ + '\n' + '* ``FilterInPlace``: ' + QgsProcessingToolboxProxyModel.Filter.InPlace.__doc__ + '\n' + '* ``FilterShowKnownIssues``: ' + QgsProcessingToolboxProxyModel.Filter.ShowKnownIssues.__doc__
# --
QgsProcessingToolboxProxyModel.Filter.baseClass = QgsProcessingToolboxProxyModel
QgsProcessingToolboxProxyModel.Filters.baseClass = QgsProcessingToolboxProxyModel
Filters = QgsProcessingToolboxProxyModel  # dirty hack since SIP seems to introduce the flags in module
