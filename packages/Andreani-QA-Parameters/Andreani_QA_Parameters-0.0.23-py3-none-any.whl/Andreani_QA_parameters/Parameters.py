import os
import platform
import sys


class Parameters:
    # CONFIGURACION PATH Y TESTCASE
    current_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
    sys.path.append(current_path)
    file_name_stored = None
    env = None

    # CONFIGURACION PARA UTILIZAR CSV DESDE SHAREPOINT
    # sharepoint_data_jmeter=None

    # CONFIGURACION FORMATO DE FECHA
    date_format = '%d/%m/%Y'
    time_format = "%H:%M:%S"

    # CONFIGURACION DE TIEMPO Y REINTENTOS PARA LA OBTENCIÓN DE ELEMENTOS
    time_between_retries = 0.5
    number_retries = 5
    highlight = True
    headless = False
    loggin_exceptions = False
    debug = False

    # CONFIGURACION DE TIEMPO Y REINTENTOS PARA LA OBTENCIÓN DE ELEMENTOS
    loggin_time = True
    
    timeout_base_sql_server = 20

    # ENTORNO POR DEFECTO
    environment = platform.system()
    if os.getenv('PYBOT_SYSTEM') is None :
        environment_configuration = "standalone" 
    else:
        environment_configuration = "server"

    # CONFIGURACION DE BROWSER Y LOGEO DE EXCEPCIONES NO ESPERADAS
    if environment_configuration == "server":
        browser = 'CHROME'
    else:
        browser = 'EDGE'

    # CONFIGURACIÓN DE GRABACION DE EVIDENCIAS
    if os.getenv('PYBOT_RECORD') is None:
        record = False
    else:
        if os.getenv('PYBOT_RECORD').lower() == "false":
            record = False
        else:
            record = True

    # VARIABLE LISTA DE PASOS
    steps_list = []

    # CONFIGURACION INCREMENTO AUTO/MANUALEXCEL
    manual_increment = False
    row = 2

    # CONFIGURACION PATH JMETER
    path_jmeter = f"C:\\Tools\\Jmeter\\bin\\jmeter.bat"
    path_jmeter_libraries_ext = f"C:\\Tools\\Jmeter\\lib\\ext"
    path_jmeter_downloads = f"{current_path}\\src\\downloads"
    path_jmeter_report_jtl = f"{path_jmeter_downloads}\\report.jtl"
    path_aggregate_report_csv_out = f"{path_jmeter_downloads}\\AggregateReport.csv"
    path_response_over_times_png_out = f"{path_jmeter_downloads}\\ResponseTimesOverTime.png"
    path_response_code_per_second_png_out = f"{path_jmeter_downloads}\\ResponseCodePerSecond.png"
    path_response_threads_state_over_time = f"{path_jmeter_downloads}\\ThreadsStateOverTime.png"
    path_dashboard = f"{current_path}src\\outputs\\dashboard_jmeter"
    path_index_html_dashboard = f"{path_dashboard}\\index.html"

    # CONFIGURACION TEST DE STRESS Y CARGA
    users_jmeter = 1
    rampup_jmeter = 1
    duration_jmeter = 1
    throughput_jmeter = 0
    url_jmeter = ""

    # CONFIGURACION PARA VALIDACION
    status_code_expected = 200
    parameter_id = None
    expected_value = ""

    server = "127.0.0.1"  # Direccion Ip de la UI desplegada por locust.
    port = 8089  # Puerto de la UI desplegada por locust.
    max_threads = 100  # Cantidad maxima de hilos (Peticiones) alcanzable.
    rate = 10  # Coeficiente incremental de carga.
    duration = 60  # Duracion de la prueba (Segundos)
    wait_time = 1  # Duracion de tiempos de espera entre peticiones.

    # CONFIGURACION PARA NOTIFICACIONES DE TEAMS
    teams_notifications_colors = "#5b5fc7"
    teams_focus_test_colors = "#383966"
