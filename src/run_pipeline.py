from dataclasses import dataclass
from enum import Enum
import yaml

from .utils import fetch_version_hash

class DBs(Enum):
    EDW = 'datasunrise01.aws2.teladoc.com'
    REDSHIFT = 'redshift.prod.livongo.com'
    
@dataclass
class ModelConfig():
    '''
    This one show how you might choose to intake model configuration parameters at run time.

    Attributes
    ----------
    learning_rate: float = 1e-3
        defaults to 1e-3 since we observed best results
    environment = 'databricks'
        this is the environment in which you're running the experiment (eg databricks, local, etc)
    experiment_name: str = None
        Use this to name your experiment and append a string to a file name. TODO: check if valid file
        naming convention
    start_date = '2020-01-01'
        the YYYY-MM-DD that the training data starts
    save_path: str = '/Users/neel.parekh/Desktop/examples/'
        where all of the outputs will live. TODO: Update all path managing to pathlib
    '''

    learning_rate: float = 1e-3
    environment = 'databricks'
    experiment_name: str = None
    start_date = '2020-01-01'
    save_path: str = '/Users/neel.parekh/Desktop/examples/'
        
    @property
    def model_path(self) -> str:
        '''
        Construct the model output file name as a property

        Parameters
        ----------

        Returns
        -------
        model_path: str
            where the model will be saved on the file system
        '''
        file_name = '_'.join(
            [str(item) for item in [self.environment, self.experiment_name, self.start_date]]
        )
        model_path = self.save_path + file_name + '.model'
        return model_path

@dataclass        
class DatabaseConfig():
    '''
    This is an example of how you might connect to one of the Teladoc databases. Still need to add
    function that will help access tables from the database, verifying table names are appropriately
    specified.

    Attributes
    ----------
    db_name: DBs
        this must be a selection of one of the enumerated `DBs` type
    entities: list[str] = None
        which tables we wish to pull from
    '''
    db_name: DBs
    entities: list[str] = None
        
    @property
    def db_conn():
        '''
        WIP
        '''
        # code to create db connection here...
        pass




if __name__ == "__main__":
    
    # Create the configs
    model_params = ModelConfig(
        learning_rate=1e-5,
        experiment_name='include_redshift_data'
    )
    EDW = DatabaseConfig(
        db_name=DBs.EDW,
        entities=['food_logs', 'weight_logs', 'voice_coach_logs']
    )


    # Get the git commit used and save it along with the input config params
    # input_config = yaml.safe_load(open(sys.argv[1]))
    input_config = {}
    input_config['git_commit'] = fetch_version_hash()

    # for debugging, print the outputs of the above configs
    print()
    print(f"INPUT_CONFIG: {input_config}")
    print(f"MODEL_SAVE_PATH: {model_params.model_path}")
    print(f"MODEL_PARAMS: {model_params}")
