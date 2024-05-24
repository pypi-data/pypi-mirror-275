import hvac
import logging
import pyodbc
class Vault:

    """
    The Vault class provides methods to authenticate and interact with Vault.

    Methods:
        - __init__(role_id, secret_id):
            Initializes the Vault class instance.

            :param role_id: The role ID to authenticate with.
            :param secret_id: The secret ID to authenticate with.

        - get_kv_secret(path, mount_point='secret', version=None):
            Retrieves a key-value secret from Vault.

            :param path: The path of the secret.
            :param mount_point: The mount point for the secret engine. Default is 'secret'.
            :param version: The version of the secret. Default is None.
            :return: The secret value.

        - get_dynamic_credentials(mount_point, database):
            Generates dynamic credentials for a database from Vault.

            :param mount_point: The mount point for the database engine.
            :param database: The name of the database.
            :return: The generated credentials (username and password).
    """

    def __init__(self, role_id, secret_id):
        """
        Initialize the class instance.

        :param role_id: The role ID to authenticate with.
        :param secret_id: The secret ID to authenticate with.
        """
        self.Client = hvac.Client(url='https://vault.mycarrier.tech')
        self.SourceCredentials = None
        try:
            self.Client.auth.approle.login(
                role_id=role_id,
                secret_id=secret_id,
            )
        except Exception as error:
            raise error
        self.ServicePrincipalCredentials = None

    def get_kv_secret(self, path, mount_point='secret', version=None):
        output = None
        if version is None:
            output = self.Client.secrets.kv.v2.read_secret_version(path=path, mount_point=mount_point)
        else:
            output = self.Client.secrets.kv.v2.read_secret_version(path=path, mount_point=mount_point, version=version)
        return output

    def get_dynamic_credentials(self, mount_point, database):
        try:
            credentials = self.Client.secrets.database.generate_credentials(
                name=database,
                mount_point=mount_point
            )
        except Exception as e:
            logging.error(msg=f"Failed to retrieve database credentials: {e}")
            raise
        output = {
            'username': credentials['username'],
            'password': credentials['password']
        }
        return output

class dbConnection:
    """
    Class for establishing a database connection and executing queries.

    Args:
        server (str): The name or IP address of the server.
        port (int): The port number of the server.
        db_name (str): The name of the database to connect to.
        driver (str, optional): The ODBC driver name. Defaults to 'ODBC Driver 18 for SQL Server'.
        encrypt (str, optional): Specify whether the connection should be encrypted. Defaults to 'yes'.
        trustservercertificate (str, optional): Specify whether to trust the server certificate. Defaults to 'no'.
        timeout (int, optional): The connection timeout in seconds. Defaults to 30.

    Attributes:
        connection: The pyodbc connection object representing the database connection.

    Methods:
        query: Executes a SQL query and returns the results.
        close: Closes the database connection.

    Examples:
        # Instantiate dbConnection
        conn = dbConnection('localhost', 1433, 'mydb')

        # Execute a query and get all results
        results = conn.query('SELECT * FROM mytable', outputResults='all')

        # Close the connection
        conn.close()
    """
    def __init__(self, server, port, db_name, driver='ODBC Driver 18 for SQL Server', encrypt='yes',
                 trustservercertificate='no', timeout=30):
        self.connection = pyodbc.connect(f"Driver={{{driver}}}; "
                          f"Server={server},{port}; "
                          f"Database={db_name}; Encrypt={encrypt}; TrustServerCertificate={trustservercertificate}; Connection Timeout={timeout}")

    def query(self, sql, outputResults: str = None, commit: bool = False):
        cursor = self.connection.cursor()
        try:
            if commit:
                self.connection.autocommit = True
            cursor.execute(sql)
            if outputResults == "one":
                return cursor.fetchone()
            if outputResults == "all":
                return cursor.fetchall()
        finally:
            cursor.close()
            self.connection.autocommit = False
    def close(self):
        self.connection.close()
