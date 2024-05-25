import sys
from google.cloud import firestore
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


class GoogleFirebaseConnector:

    def __init__(self, credentials_file_path):
        """
        :param credentials_file_path: Ruta hasta el archivo de las credenciales, ej. base-de-datos-f7431-firebase-adminsdk-4sa5k-fi919245c12.json"
        """
        self.credentials_file_path = credentials_file_path
        self.db = self.init_database()

    def init_database(self):
        print("[FIREBASE]: Iniciando Firebase...\n", file=sys.stdout)
        # Inicializa el SDK de Firebase
        cred = credentials.Certificate(self.credentials_file_path)
        firebase_admin.initialize_app(cred)

        # Conéctate a Firestore
        db = firestore.client()

        return db

    """
    :param path: Ruta hasta la ubicación donde queremos obtener datos, ej. anime/anime-by-letter/downloads/animelist.
    :param target: Es de donde se obtendran los datos cuando llegue al documento, de un array un map con el nombre "xxx".
    """

    def getDataByPath(self, path: str, target: str):
        path_splitted = path.split('/')

        # Verificar que el número de elementos en path_splited es par
        if len(path_splitted) % 2 != 0:
            raise ValueError(
                "[Error][getDataByPath()]: El número de elementos en el path debe ser par para su correcto funcionamiento.")

        # Comenzar desde la primera colección especificada en el path
        ref = self.db.collection(path_splitted[0])

        # Recorrer el path en pares de (colección, documento)
        for i in range(1, len(path_splitted), 2):
            document_name = path_splitted[i]

            # Acceder al documento correspondiente
            ref = ref.document(document_name)

            # Sí hay más elementos en el path, acceder a la siguiente colección
            if i + 1 < len(path_splitted):
                ref = ref.collection(path_splitted[i + 1])

        # Obtener el documento final
        doc = ref.get().to_dict()

        # Verificar que el documento existe y contiene el target
        if doc is None or target not in doc:
            raise ValueError(f"[Error][getDataByPath()]: El documento no contiene el objetivo '{target}' o no existe.")

        # Obtener los datos del target
        data = doc[target]

        # Imprimimos mensaje para avisar de que se está descargando
        print(f'[getDataByPath()]: Descargando la información de "{path}/{target}"...\n', file=sys.stdout)

        # Devolver los datos.
        return data
