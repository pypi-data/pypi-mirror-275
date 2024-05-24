import os
from uuid import uuid4

from universal_common_configuration import ConfigurationBuilder, IConfiguration, IConfigurationSection
import universal_common_configuration.environment_variables
import universal_common_configuration.user_secrets

class TestConfiguration:
    def test_create_configuration_environment_variables(self):
        random_string: str = str(uuid4())
        os.environ["TEST"] = random_string
        configuration: IConfiguration = ConfigurationBuilder().add_environment_variables().build()
        assert configuration["TEST"] == random_string

    def test_can_create_sections_from_environment_variables(self):
        random_string: str = str(uuid4())
        os.environ["ConnectionStrings:Database"] = random_string
        configuration: IConfiguration = ConfigurationBuilder().add_environment_variables().build()
        configurationSection: IConfigurationSection = configuration.get_section("ConnectionStrings")
        assert configurationSection is not None
        assert configurationSection["Database"] == random_string
        assert configuration.get_connection_string("Database") == random_string

    def test_non_existent_user_secrets_doesnt_crash(self):
        ConfigurationBuilder().add_user_secrets("asdf").build()