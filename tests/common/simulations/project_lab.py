import os
from .project_simulator import ProjectSimulator, PkgSimulator
from .lm_simulator import LmSimulator
from .arm_simulator import ArmSimulator

TEMPLATES = 'templates'
GENERAL_TEMPLATES_GROUP = 'general'
ASSEMBLY_TEMPLATES_GROUP = 'assemblies'
RESOURCE_TEMPLATES_GROUP = 'resources'
TYPE_TEMPLATES_GROUP = 'types'
ANSIBLE_RM_RESOURCE_GROUP = 'ansiblerm'
BRENT_RESOURCE_GROUP = 'brent'
BRENT_2DOT1_RESOURCE_GROUP = 'brent2dot1'

SUBPROJECTS_GROUP = 'subprojects'

ASSEMBLY_BASIC = 'basic'
ASSEMBLY_WITH_BEHAVIOUR = 'with_behaviour'
ASSEMBLY_WITH_YAML_PROJECT_FILE_PROJECT = 'with_yaml_project_file'
INVALID_ASSEMBLY_NON_JSON_CONFIGURATION = 'invalid_non_json_configuration'
INVALID_ASSEMBLY_NON_JSON_RUNTIME = 'invalid_non_json_runtime'
INVALID_ASSEMBLY_NON_JSON_TEST = 'invalid_non_json_test'
INVALID_ASSEMBLY_INVALID_JSON_CONFIGURATION = 'invalid_json_configuration'
INVALID_ASSEMBLY_INVALID_JSON_RUNTIME = 'invalid_json_runtime'
INVALID_ASSEMBLY_INVALID_JSON_TEST = 'invalid_json_test'
INVALID_ASSEMBLY_NO_DESCRIPTOR = 'invalid_no_descriptor'
INVALID_ASSEMBLY_MISMATCH_DESCRIPTOR_NAME = 'invalid_mismatch_descriptor_name'
INVALID_ASSEMBLY_MISMATCH_DESCRIPTOR_TEMPLATE_NAME = 'invalid_mismatch_descriptor_template_name'
ASSEMBLY_CONTAINS_ASSEMBLY_BASIC = 'contains_basic'
ASSEMBLY_CONTAINS_ASSEMBLY_WITH_BEHAVIOUR = 'contains_with_behaviour'
ASSEMBLY_CONTAINS_INVALID_ASSEMBLY_NON_JSON_CONFIGURATION = 'contains_invalid_non_json_configuration'
ASSEMBLY_CONTAINS_INVALID_ASSEMBLY_NON_JSON_RUNTIME = 'contains_invalid_non_json_runtime'
ASSEMBLY_CONTAINS_INVALID_ASSEMBLY_NON_JSON_TEST = 'contains_invalid_non_json_test'
ASSEMBLY_CONTAINS_INVALID_ASSEMBLY_INVALID_JSON_CONFIGURATION = 'contains_invalid_json_configuration'
ASSEMBLY_CONTAINS_INVALID_ASSEMBLY_INVALID_JSON_RUNTIME = 'contains_invalid_json_runtime'
ASSEMBLY_CONTAINS_INVALID_ASSEMBLY_INVALID_JSON_TEST = 'contains_invalid_json_test'
ASSEMBLY_CONTAINS_INVALID_ASSEMBLY_NO_DESCRIPTOR = 'contains_invalid_no_descriptor'
ASSEMBLY_CONTAINS_INVALID_ASSEMBLY_MISMATCH_DESCRIPTOR_NAME = 'contains_invalid_mismatch_descriptor_name'
ASSEMBLY_CONTAINS_ARM_BASIC = 'contains_basic'
ASSEMBLY_CONTAINS_INVALID_ARM_NO_DESCRIPTOR = 'contains_invalid_no_descriptor'
ASSEMBLY_CONTAINS_INVALID_ARM_NO_LIFECYCLE = 'contains_invalid_no_lifecycle'
ASSEMBLY_CONTAINS_INVALID_ARM_NO_MANIFEST = 'contains_invalid_no_manifest'
ASSEMBLY_CONTAINS_INVALID_ARM_MISMATCH_DESCRIPTOR_NAME = 'contains_invalid_mismatch_descriptor_name'
ASSEMBLY_CONTAINS_BRENT_BASIC = 'contains_basic'
ASSEMBLY_CONTAINS_INVALID_BRENT_NO_DEFINITIONS = 'contains_invalid_no_definitions'
ASSEMBLY_CONTAINS_INVALID_BRENT_NO_LM_DEFINITIONS = 'contains_invalid_no_lm_definitions'
ASSEMBLY_CONTAINS_INVALID_BRENT_NO_LM_DESCRIPTOR = 'contains_invalid_no_lm_descriptor'
ASSEMBLY_CONTAINS_INVALID_BRENT_MISMATCH_DESCRIPTOR_NAME = 'contains_invalid_mismatch_descriptor_name'
ASSEMBLY_CONTAINS_INVALID_BRENT_NO_LIFECYCLE = 'contains_invalid_no_lifecycle'
ASSEMBLY_WITH_OLD_STYLE = 'old_style'
ASSEMBLY_WITH_DESCRIPTOR_REFERENCES = 'with_descriptor_references'
ASSEMBLY_WITH_BEHAVIOUR_REFERENCES = 'with_behaviour_references'
ASSEMBLY_WITH_UNRESOLVABLE_REFERENCES = 'with_unresolvable_references'
ASSEMBLY_WITH_TEMPLATE = 'with_template'

SUBPROJECT_NAME_ASSEMBLY_BASIC = 'sub_basic'
SUBPROJECT_NAME_ASSEMBLY_WITH_BEHAVIOUR = 'sub_with_behaviour'
SUBPROJECT_NAME_INVALID_ASSEMBLY_NON_JSON_CONFIGURATION = 'sub_invalid_non_json_configuration'
SUBPROJECT_NAME_INVALID_ASSEMBLY_NON_JSON_RUNTIME = 'sub_invalid_non_json_runtime'
SUBPROJECT_NAME_INVALID_ASSEMBLY_NON_JSON_TEST = 'sub_invalid_non_json_test'
SUBPROJECT_NAME_INVALID_ASSEMBLY_INVALID_JSON_CONFIGURATION = 'sub_invalid_json_configuration'
SUBPROJECT_NAME_INVALID_ASSEMBLY_INVALID_JSON_RUNTIME = 'sub_invalid_json_runtime'
SUBPROJECT_NAME_INVALID_ASSEMBLY_INVALID_JSON_TEST = 'sub_invalid_json_test'
SUBPROJECT_NAME_INVALID_ASSEMBLY_NO_DESCRIPTOR = 'sub_invalid_no_descriptor'
SUBPROJECT_NAME_INVALID_ASSEMBLY_MISMATCH_DESCRIPTOR_NAME = 'sub_invalid_mismatch_descriptor_name'
SUBPROJECT_NAME_ARM_BASIC = 'sub_basic'
SUBPROJECT_NAME_INVALID_ARM_NO_DESCRIPTOR = 'sub_invalid_no_descriptor'
SUBPROJECT_NAME_INVALID_ARM_NO_LIFECYCLE = 'sub_invalid_no_lifecycle'
SUBPROJECT_NAME_INVALID_ARM_NO_MANIFEST = 'sub_invalid_no_manifest'
SUBPROJECT_NAME_INVALID_ARM_MISMATCH_DESCRIPTOR_NAME = 'sub_invalid_mismatch_descriptor_name'
SUBPROJECT_NAME_BRENT_BASIC = 'sub_basic'
SUBPROJECT_NAME_INVALID_BRENT_MISMATCH_DESCRIPTOR_NAME = 'sub_invalid_mismatch_descriptor_name'
SUBPROJECT_NAME_INVALID_BRENT_NO_DEFINITIONS = 'sub_invalid_no_definitions'
SUBPROJECT_NAME_INVALID_BRENT_NO_INFRASTRUCTURE = 'sub_invalid_no_infrastructure'
SUBPROJECT_NAME_INVALID_BRENT_NO_LM_DEFINITIONS = 'sub_invalid_no_lm_definitions'
SUBPROJECT_NAME_INVALID_BRENT_NO_DESCRIPTOR = 'sub_invalid_no_lm_descriptor'
SUBPROJECT_NAME_INVALID_BRENT_NO_LIFECYCLE = 'sub_invalid_no_lifecycle'
SUBPROJECT_NAME_BRENT_2DOT1_BASIC = 'sub_basic'

ARM_BASIC = 'basic'
INVALID_ARM_NO_DESCRIPTOR = 'invalid_no_descriptor'
INVALID_ARM_NO_LIFECYCLE = 'invalid_no_lifecycle'
INVALID_ARM_NO_MANIFEST = 'invalid_no_manifest'
INVALID_ARM_MISMATCH_DESCRIPTOR_NAME = 'invalid_mismatch_descriptor_name'

BRENT_BASIC = 'basic'
BRENT_PREALPHA_STYLE = 'prealpha-style'
INVALID_BRENT_NO_DEFINITIONS = 'invalid_no_definitions'
INVALID_BRENT_NO_LM_DEFINITIONS = 'invalid_no_lm_definitions'
INVALID_BRENT_NO_LM_DESCRIPTOR = 'invalid_no_lm_descriptor'
INVALID_BRENT_MISMATCH_DESCRIPTOR_NAME = 'invalid_mismatch_lm_descriptor_name'
INVALID_BRENT_NO_LIFECYCLE = 'invalid_no_lifecycle'
BRENT_WITH_INFRASTRUCTURE_TEMPLATES = 'with_infrastructure_templates'
BRENT_WITH_MISSING_DRIVER_SELECTOR = 'with_missing_driver_selector'
BRENT_TOSCA = 'with_tosca'

BRENT_2DOT1_BASIC = 'basic'
BRENT_2DOT1_PREALPHA_STYLE = 'prealpha-style'
INVALID_BRENT_2DOT1_NO_DEFINITIONS = 'invalid_no_definitions'
INVALID_BRENT_2DOT1_NO_INFRASTRUCTURE = 'invalid_no_infrastructure'
INVALID_BRENT_2DOT1_NO_LM_DEFINITIONS = 'invalid_no_lm_definitions'
INVALID_BRENT_2DOT1_NO_LM_DESCRIPTOR = 'invalid_no_lm_descriptor'
INVALID_BRENT_2DOT1_MISMATCH_DESCRIPTOR_NAME = 'invalid_mismatch_lm_descriptor_name'
INVALID_BRENT_2DOT1_NO_LIFECYCLE = 'invalid_no_lifecycle'
BRENT_2DOT1_WITH_EMPTY_INFRASTRUCTURE = 'with_empty_infrastructure'

TYPE_BASIC = 'basic'
TYPE_WITH_BEHAVIOUR = 'with_behaviour'

PKG_ASSEMBLY_BASIC = 'basic-1.0.tgz'
PKG_ASSEMBLY_WITH_TEMPLATE = 'with_template-1.0.tgz'
PKG_ASSEMBLY_DEPRECATED_CONTENT_BASIC = 'deprecated-content-basic-1.0.tgz'
PKG_ASSEMBLY_WITH_BEHAVIOUR = 'with_behaviour-1.0.tgz'
PKG_ASSEMBLY_WITH_BEHAVIOUR_MULTI_TESTS = 'with_behaviour_multi_tests-1.0.tgz'
PKG_ASSEMBLY_WITH_SCENARIO_REF_MISSING_CONFIG = 'with_scenario_referencing_missing_config-1.0.tgz'
PKG_ASSEMBLY_CONTAINS_ASSEMBLY_BASIC = 'contains_basic-1.0.tgz'
PKG_ASSEMBLY_CONTAINS_ASSEMBLY_WITH_BEHAVIOUR = 'contains_with_behaviour-1.0.tgz'
PKG_ASSEMBLY_CONTAINS_ASSEMBLY_WITH_BEHAVIOUR_MULTI_TESTS = 'contains_with_behaviour_multi_tests-1.0.tgz'
PKG_ASSEMBLY_CONTAINS_ARM_BASIC = 'contains_basic-1.0.tgz'
PKG_ASSEMBLY_OLD_STYLE = 'old_style-1.0.tgz'
PKG_ASSEMBLY_CONTAINS_BRENT_BASIC = 'contains_basic-1.0.tgz'
PKG_ASSEMBLY_CONTAINS_BRENT_2DOT1_BASIC = 'contains_basic-1.0.tgz'

PKG_ARM_BASIC = 'basic-1.0.tgz'

PKG_BRENT_BASIC = 'basic-1.0.tgz'
PKG_BRENT_2DOT1_BASIC = 'basic-1.0.tgz'
PKG_BRENT_TOSCA = 'with_tosca-1.0.csar'

PKG_INVALID_ZIP = 'invalid_zip-1.0.zip'

PKG_TYPE_BASIC = 'basic-1.0.tgz'
PKG_TYPE_WITH_BEHAVIOUR = 'with_behaviour-1.0.tgz'

def templates_path():
    return os.path.join(os.path.dirname(__file__), TEMPLATES)


def assembly_template_path(template_name):
    return os.path.join(templates_path(), ASSEMBLY_TEMPLATES_GROUP, template_name)

def general_pkg_path(pkg_name):
    return os.path.join(templates_path(), GENERAL_TEMPLATES_GROUP, pkg_name)

def assembly_pkg_path(pkg_name):
    return os.path.join(templates_path(), ASSEMBLY_TEMPLATES_GROUP, pkg_name)

def assembly_subproject_template_path(subproject_group, template_name):
    return os.path.join(templates_path(), ASSEMBLY_TEMPLATES_GROUP, SUBPROJECTS_GROUP, subproject_group, template_name)

def assembly_subproject_pkg_path(subproject_group, pkg_name):
    return os.path.join(templates_path(), ASSEMBLY_TEMPLATES_GROUP, SUBPROJECTS_GROUP, subproject_group, pkg_name)

def resource_template_path(resource_type, template_name):
    return os.path.join(templates_path(), RESOURCE_TEMPLATES_GROUP, resource_type, template_name)

def resource_pkg_path(resource_type, pkg_name):
    return os.path.join(templates_path(), RESOURCE_TEMPLATES_GROUP, resource_type, pkg_name)

def type_template_path(template_name):
    return os.path.join(templates_path(), TYPE_TEMPLATES_GROUP, template_name)

def type_pkg_path(pkg_name):
    return os.path.join(templates_path(), TYPE_TEMPLATES_GROUP, pkg_name)

class ProjectSimLab:

    def __init__(self):
        self.simulations = []

    def destroySims(self):
        for sim in self.simulations:
            sim.destroy()

    def __sim_project(self, template_path):
        simulator = ProjectSimulator(template_path)
        sim = simulator.start()
        self.simulations.append(sim)
        return sim

    def __sim_pkg(self, pkg_template_path):
        simulator = PkgSimulator(pkg_template_path)
        sim = simulator.start()
        self.simulations.append(sim)
        return sim

    def simulate_assembly_basic(self):
        return self.__sim_project(assembly_template_path(ASSEMBLY_BASIC))

    def simulate_assembly_old_style(self):
        return self.__sim_project(assembly_template_path(ASSEMBLY_WITH_OLD_STYLE))

    def simulate_assembly_with_descriptor_references(self):
        return self.__sim_project(assembly_template_path(ASSEMBLY_WITH_DESCRIPTOR_REFERENCES))

    def simulate_assembly_with_behaviour_references(self):
        return self.__sim_project(assembly_template_path(ASSEMBLY_WITH_BEHAVIOUR_REFERENCES))

    def simulate_assembly_with_unresolvable_references(self):
        return self.__sim_project(assembly_template_path(ASSEMBLY_WITH_UNRESOLVABLE_REFERENCES))
    
    def simulate_assembly_with_template(self):
        return self.__sim_project(assembly_template_path(ASSEMBLY_WITH_TEMPLATE))

    def simulate_assembly_with_yaml_project_file(self):
        return self.__sim_project(assembly_template_path(ASSEMBLY_WITH_YAML_PROJECT_FILE_PROJECT))

    def simulate_invalid_assembly_no_descriptor(self):
        return self.__sim_project(assembly_template_path(INVALID_ASSEMBLY_NO_DESCRIPTOR))

    def simulate_invalid_assembly_mismatch_descriptor_name(self):
        return self.__sim_project(assembly_template_path(INVALID_ASSEMBLY_MISMATCH_DESCRIPTOR_NAME))

    def simulate_invalid_assembly_mismatch_descriptor_template_name(self):
        return self.__sim_project(assembly_template_path(INVALID_ASSEMBLY_MISMATCH_DESCRIPTOR_TEMPLATE_NAME))

    def simulate_assembly_with_behaviour(self):
        return self.__sim_project(assembly_template_path(ASSEMBLY_WITH_BEHAVIOUR))

    def simulate_invalid_assembly_non_json_configuration(self):
        return self.__sim_project(assembly_template_path(INVALID_ASSEMBLY_NON_JSON_CONFIGURATION))

    def simulate_invalid_assembly_non_json_runtime(self):
        return self.__sim_project(assembly_template_path(INVALID_ASSEMBLY_NON_JSON_RUNTIME))

    def simulate_invalid_assembly_non_json_test(self):
        return self.__sim_project(assembly_template_path(INVALID_ASSEMBLY_NON_JSON_TEST))

    def simulate_invalid_assembly_invalid_json_configuration(self):
        return self.__sim_project(assembly_template_path(INVALID_ASSEMBLY_INVALID_JSON_CONFIGURATION))

    def simulate_invalid_assembly_invalid_json_runtime(self):
        return self.__sim_project(assembly_template_path(INVALID_ASSEMBLY_INVALID_JSON_RUNTIME))

    def simulate_invalid_assembly_invalid_json_test(self):
        return self.__sim_project(assembly_template_path(INVALID_ASSEMBLY_INVALID_JSON_TEST))

    def simulate_assembly_contains_assembly_basic(self):
        return self.__sim_project(assembly_subproject_template_path(ASSEMBLY_TEMPLATES_GROUP, ASSEMBLY_CONTAINS_ASSEMBLY_BASIC))

    def simulate_assembly_contains_assembly_with_behaviour(self):
        return self.__sim_project(assembly_subproject_template_path(ASSEMBLY_TEMPLATES_GROUP, ASSEMBLY_CONTAINS_ASSEMBLY_WITH_BEHAVIOUR))
    
    def simulate_assembly_contains_invalid_assembly_no_descriptor(self):
        return self.__sim_project(assembly_subproject_template_path(ASSEMBLY_TEMPLATES_GROUP, ASSEMBLY_CONTAINS_INVALID_ASSEMBLY_NO_DESCRIPTOR))

    def simulate_assembly_contains_invalid_assembly_mismatch_descriptor_name(self):
        return self.__sim_project(assembly_subproject_template_path(ASSEMBLY_TEMPLATES_GROUP, ASSEMBLY_CONTAINS_INVALID_ASSEMBLY_MISMATCH_DESCRIPTOR_NAME))
    
    def simulate_assembly_contains_invalid_assembly_non_json_configuration(self):
        return self.__sim_project(assembly_subproject_template_path(ASSEMBLY_TEMPLATES_GROUP, ASSEMBLY_CONTAINS_INVALID_ASSEMBLY_NON_JSON_CONFIGURATION))

    def simulate_assembly_contains_invalid_assembly_non_json_runtime(self):
        return self.__sim_project(assembly_subproject_template_path(ASSEMBLY_TEMPLATES_GROUP, ASSEMBLY_CONTAINS_INVALID_ASSEMBLY_NON_JSON_RUNTIME))

    def simulate_assembly_contains_invalid_assembly_non_json_test(self):
        return self.__sim_project(assembly_subproject_template_path(ASSEMBLY_TEMPLATES_GROUP, ASSEMBLY_CONTAINS_INVALID_ASSEMBLY_NON_JSON_TEST))

    def simulate_assembly_contains_invalid_assembly_invalid_json_configuration(self):
        return self.__sim_project(assembly_subproject_template_path(ASSEMBLY_TEMPLATES_GROUP, ASSEMBLY_CONTAINS_INVALID_ASSEMBLY_INVALID_JSON_CONFIGURATION))

    def simulate_assembly_contains_invalid_assembly_invalid_json_runtime(self):
        return self.__sim_project(assembly_subproject_template_path(ASSEMBLY_TEMPLATES_GROUP, ASSEMBLY_CONTAINS_INVALID_ASSEMBLY_INVALID_JSON_RUNTIME))

    def simulate_assembly_contains_invalid_assembly_invalid_json_test(self):
        return self.__sim_project(assembly_subproject_template_path(ASSEMBLY_TEMPLATES_GROUP, ASSEMBLY_CONTAINS_INVALID_ASSEMBLY_INVALID_JSON_TEST))

    def simulate_brent_basic(self):
        return self.__sim_project(resource_template_path(BRENT_RESOURCE_GROUP, BRENT_BASIC))

    def simulate_brent_tosca(self):
        return self.__sim_project(resource_template_path(BRENT_RESOURCE_GROUP, BRENT_TOSCA))

    def simulate_brent_with_missing_driver_selector(self):
        return self.__sim_project(resource_template_path(BRENT_RESOURCE_GROUP, BRENT_WITH_MISSING_DRIVER_SELECTOR))

    def simulate_brent_with_infrastructure_templates(self):
        return self.__sim_project(resource_template_path(BRENT_RESOURCE_GROUP, BRENT_WITH_INFRASTRUCTURE_TEMPLATES))

    def simulate_brent_with_prealpha_style(self):
        return self.__sim_project(resource_template_path(BRENT_RESOURCE_GROUP, BRENT_PREALPHA_STYLE))

    def simulate_invalid_brent_mismatch_descriptor_name(self):
        return self.__sim_project(resource_template_path(BRENT_RESOURCE_GROUP, INVALID_BRENT_MISMATCH_DESCRIPTOR_NAME))

    def simulate_invalid_brent_no_definitions(self):
        return self.__sim_project(resource_template_path(BRENT_RESOURCE_GROUP, INVALID_BRENT_NO_DEFINITIONS))

    def simulate_invalid_brent_no_lm_definitions(self):
        return self.__sim_project(resource_template_path(BRENT_RESOURCE_GROUP, INVALID_BRENT_NO_LM_DEFINITIONS))

    def simulate_invalid_brent_no_lm_descriptor(self):
        return self.__sim_project(resource_template_path(BRENT_RESOURCE_GROUP, INVALID_BRENT_NO_LM_DESCRIPTOR))

    def simulate_invalid_brent_no_lifecycle(self):
        return self.__sim_project(resource_template_path(BRENT_RESOURCE_GROUP, INVALID_BRENT_NO_LIFECYCLE))

    def simulate_assembly_contains_brent_basic(self):
        return self.__sim_project(assembly_subproject_template_path(os.path.join(RESOURCE_TEMPLATES_GROUP, BRENT_RESOURCE_GROUP), ASSEMBLY_CONTAINS_BRENT_BASIC))
    
    def simulate_assembly_contains_brent_2dot1_basic(self):
        return self.__sim_project(assembly_subproject_template_path(os.path.join(RESOURCE_TEMPLATES_GROUP, BRENT_2DOT1_RESOURCE_GROUP), ASSEMBLY_CONTAINS_BRENT_BASIC))

    def simulate_assembly_contains_invalid_brent_mismatch_descriptor_name(self):
        return self.__sim_project(assembly_subproject_template_path(os.path.join(RESOURCE_TEMPLATES_GROUP, BRENT_RESOURCE_GROUP), ASSEMBLY_CONTAINS_INVALID_BRENT_MISMATCH_DESCRIPTOR_NAME))

    def simulate_assembly_contains_invalid_brent_no_definitions(self):
        return self.__sim_project(assembly_subproject_template_path(os.path.join(RESOURCE_TEMPLATES_GROUP, BRENT_RESOURCE_GROUP), ASSEMBLY_CONTAINS_INVALID_BRENT_NO_DEFINITIONS))

    def simulate_assembly_contains_invalid_brent_no_lm_definitions(self):
        return self.__sim_project(assembly_subproject_template_path(os.path.join(RESOURCE_TEMPLATES_GROUP, BRENT_RESOURCE_GROUP), ASSEMBLY_CONTAINS_INVALID_BRENT_NO_LM_DEFINITIONS))

    def simulate_assembly_contains_invalid_brent_no_lm_descriptor(self):
        return self.__sim_project(assembly_subproject_template_path(os.path.join(RESOURCE_TEMPLATES_GROUP, BRENT_RESOURCE_GROUP), ASSEMBLY_CONTAINS_INVALID_BRENT_NO_LM_DESCRIPTOR))

    def simulate_assembly_contains_invalid_brent_no_lifecycle(self):
        return self.__sim_project(assembly_subproject_template_path(os.path.join(RESOURCE_TEMPLATES_GROUP, BRENT_RESOURCE_GROUP), ASSEMBLY_CONTAINS_INVALID_BRENT_NO_LIFECYCLE))

    def simulate_arm_basic(self):
        return self.__sim_project(resource_template_path(ANSIBLE_RM_RESOURCE_GROUP, ARM_BASIC))

    def simulate_invalid_arm_no_descriptor(self):
        return self.__sim_project(resource_template_path(ANSIBLE_RM_RESOURCE_GROUP, INVALID_ARM_NO_DESCRIPTOR))

    def simulate_invalid_arm_no_lifecycle(self):
        return self.__sim_project(resource_template_path(ANSIBLE_RM_RESOURCE_GROUP, INVALID_ARM_NO_LIFECYCLE))

    def simulate_invalid_arm_no_manifest(self):
        return self.__sim_project(resource_template_path(ANSIBLE_RM_RESOURCE_GROUP, INVALID_ARM_NO_MANIFEST))

    def simulate_invalid_arm_mismatch_descriptor_name(self):
        return self.__sim_project(resource_template_path(ANSIBLE_RM_RESOURCE_GROUP, INVALID_ARM_MISMATCH_DESCRIPTOR_NAME))

    def simulate_assembly_contains_arm_basic(self):
        return self.__sim_project(assembly_subproject_template_path(os.path.join(RESOURCE_TEMPLATES_GROUP, ANSIBLE_RM_RESOURCE_GROUP), ASSEMBLY_CONTAINS_ARM_BASIC))

    def simulate_assembly_contains_invalid_arm_no_descriptor(self):
        return self.__sim_project(assembly_subproject_template_path(os.path.join(RESOURCE_TEMPLATES_GROUP, ANSIBLE_RM_RESOURCE_GROUP), ASSEMBLY_CONTAINS_INVALID_ARM_NO_DESCRIPTOR))

    def simulate_assembly_contains_invalid_arm_no_lifecycle(self):
        return self.__sim_project(assembly_subproject_template_path(os.path.join(RESOURCE_TEMPLATES_GROUP, ANSIBLE_RM_RESOURCE_GROUP), ASSEMBLY_CONTAINS_INVALID_ARM_NO_LIFECYCLE))

    def simulate_assembly_contains_invalid_arm_no_manifest(self):
        return self.__sim_project(assembly_subproject_template_path(os.path.join(RESOURCE_TEMPLATES_GROUP, ANSIBLE_RM_RESOURCE_GROUP), ASSEMBLY_CONTAINS_INVALID_ARM_NO_MANIFEST))

    def simulate_assembly_contains_invalid_arm_mismatch_descriptor_name(self):
        return self.__sim_project(assembly_subproject_template_path(os.path.join(RESOURCE_TEMPLATES_GROUP, ANSIBLE_RM_RESOURCE_GROUP), ASSEMBLY_CONTAINS_INVALID_ARM_MISMATCH_DESCRIPTOR_NAME))

    def simulate_brent_2dot1_basic(self):
        return self.__sim_project(resource_template_path(BRENT_2DOT1_RESOURCE_GROUP, BRENT_BASIC))

    def simulate_brent_2dot1_with_empty_infrastructure(self):
        project = self.__sim_project(resource_template_path(BRENT_2DOT1_RESOURCE_GROUP, BRENT_2DOT1_WITH_EMPTY_INFRASTRUCTURE))
        os.remove(os.path.join(project.path, 'Definitions', 'infrastructure', '.gitkeep'))
        return project

    def simulate_brent_2dot1_with_prealpha_style(self):
        return self.__sim_project(resource_template_path(BRENT_2DOT1_RESOURCE_GROUP, BRENT_2DOT1_PREALPHA_STYLE))

    def simulate_invalid_brent_2dot1_mismatch_descriptor_name(self):
        return self.__sim_project(resource_template_path(BRENT_2DOT1_RESOURCE_GROUP, INVALID_BRENT_2DOT1_MISMATCH_DESCRIPTOR_NAME))

    def simulate_invalid_brent_2dot1_no_definitions(self):
        return self.__sim_project(resource_template_path(BRENT_2DOT1_RESOURCE_GROUP, INVALID_BRENT_2DOT1_NO_DEFINITIONS))

    def simulate_invalid_brent_2dot1_no_infrastructure(self):
        return self.__sim_project(resource_template_path(BRENT_2DOT1_RESOURCE_GROUP, INVALID_BRENT_2DOT1_NO_INFRASTRUCTURE))

    def simulate_invalid_brent_2dot1_no_lm_definitions(self):
        return self.__sim_project(resource_template_path(BRENT_2DOT1_RESOURCE_GROUP, INVALID_BRENT_2DOT1_NO_LM_DEFINITIONS))

    def simulate_invalid_brent_2dot1_no_lm_descriptor(self):
        return self.__sim_project(resource_template_path(BRENT_2DOT1_RESOURCE_GROUP, INVALID_BRENT_2DOT1_NO_LM_DESCRIPTOR))

    def simulate_invalid_brent_2dot1_no_lifecycle(self):
        return self.__sim_project(resource_template_path(BRENT_2DOT1_RESOURCE_GROUP, INVALID_BRENT_2DOT1_NO_LIFECYCLE))

    def simulate_type_basic(self):
        return self.__sim_project(type_template_path(TYPE_BASIC))

    def simulate_type_with_behaviour(self):
        return self.__sim_project(type_template_path(TYPE_WITH_BEHAVIOUR))

    def simulate_pkg_general_invalid_zip(self):
        return self.__sim_pkg(general_pkg_path(PKG_INVALID_ZIP))

    def simulate_pkg_assembly_basic(self):
        return self.__sim_pkg(assembly_pkg_path(PKG_ASSEMBLY_BASIC))

    def simulate_pkg_assembly_with_template(self):
        return self.__sim_pkg(assembly_pkg_path(PKG_ASSEMBLY_WITH_TEMPLATE))

    def simulate_pkg_assembly_deprecated_content_basic(self):
        return self.__sim_pkg(assembly_pkg_path(PKG_ASSEMBLY_DEPRECATED_CONTENT_BASIC))

    def simulate_pkg_assembly_with_scenario_referencing_missing_config(self):
        return self.__sim_pkg(assembly_pkg_path(PKG_ASSEMBLY_WITH_SCENARIO_REF_MISSING_CONFIG))

    def simulate_pkg_assembly_old_style(self):
        return self.__sim_pkg(assembly_pkg_path(PKG_ASSEMBLY_OLD_STYLE))
    
    def simulate_pkg_assembly_with_behaviour(self):
        return self.__sim_pkg(assembly_pkg_path(PKG_ASSEMBLY_WITH_BEHAVIOUR))

    def simulate_pkg_assembly_with_behaviour_multi_tests(self):
        return self.__sim_pkg(assembly_pkg_path(PKG_ASSEMBLY_WITH_BEHAVIOUR_MULTI_TESTS))

    def simulate_pkg_assembly_contains_assembly_basic(self):
        return self.__sim_pkg(assembly_subproject_pkg_path(ASSEMBLY_TEMPLATES_GROUP, PKG_ASSEMBLY_CONTAINS_ASSEMBLY_BASIC))

    def simulate_pkg_assembly_contains_assembly_with_behaviour(self):
        return self.__sim_pkg(assembly_subproject_pkg_path(ASSEMBLY_TEMPLATES_GROUP, PKG_ASSEMBLY_CONTAINS_ASSEMBLY_WITH_BEHAVIOUR))

    def simulate_pkg_assembly_contains_assembly_with_behaviour_multi_tests(self):
        return self.__sim_pkg(assembly_subproject_pkg_path(ASSEMBLY_TEMPLATES_GROUP, PKG_ASSEMBLY_CONTAINS_ASSEMBLY_WITH_BEHAVIOUR_MULTI_TESTS))

    def simulate_pkg_arm_basic(self):
        return self.__sim_pkg(resource_pkg_path(ANSIBLE_RM_RESOURCE_GROUP, PKG_ARM_BASIC))

    def simulate_pkg_assembly_contains_arm_basic(self):
        return self.__sim_pkg(assembly_subproject_pkg_path(os.path.join(RESOURCE_TEMPLATES_GROUP, ANSIBLE_RM_RESOURCE_GROUP), PKG_ASSEMBLY_CONTAINS_ARM_BASIC))

    def simulate_pkg_brent_basic(self):
        return self.__sim_pkg(resource_pkg_path(BRENT_RESOURCE_GROUP, PKG_BRENT_BASIC))

    def simulate_pkg_brent_tosca(self):
        return self.__sim_pkg(resource_pkg_path(BRENT_RESOURCE_GROUP, PKG_BRENT_TOSCA))

    def simulate_pkg_brent_2dot1_basic(self):
        return self.__sim_pkg(resource_pkg_path(BRENT_2DOT1_RESOURCE_GROUP, PKG_BRENT_2DOT1_BASIC))

    def simulate_pkg_assembly_contains_brent_basic(self):
        return self.__sim_pkg(assembly_subproject_pkg_path(os.path.join(RESOURCE_TEMPLATES_GROUP, BRENT_RESOURCE_GROUP), PKG_ASSEMBLY_CONTAINS_BRENT_BASIC))

    def simulate_pkg_assembly_contains_brent_2dot1_basic(self):
        return self.__sim_pkg(assembly_subproject_pkg_path(os.path.join(RESOURCE_TEMPLATES_GROUP, BRENT_2DOT1_RESOURCE_GROUP), PKG_ASSEMBLY_CONTAINS_BRENT_2DOT1_BASIC))

    def simulate_pkg_type_basic(self):
        return self.__sim_pkg(type_pkg_path(PKG_TYPE_BASIC))

    def simulate_pkg_type_with_behaviour(self):
        return self.__sim_pkg(type_pkg_path(PKG_TYPE_WITH_BEHAVIOUR))

    def simulate_lm(self):
        return LmSimulator().start()

    def simulate_arm(self):
        return ArmSimulator().start()