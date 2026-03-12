
# --------------------------- PARSERING

def parser_print(input, words_number=8):
    array_words = input.split()
    for k in range(len(array_words)//words_number + 1):
        print(plas(array_words, k, words_number))

# print_list_as_string
def plas(list, iteration, words_number):
    return " ".join(list[(iteration*words_number):(iteration+1)*words_number])

def compare_two_strings(input1, input2, words_number=6, padding=30):
    input_array1 = input1.split()
    input_array2 = input2.split()
    for k in range(len(input_array1)//words_number + 1):
        print(plas(input_array1, k, words_number).ljust(padding," ") + "| " + plas(input_array2, k, words_number))
        if k % 5 == 0:
            print("-"*(padding*2+1))


# ----------------------------- TRANSCRIBE
DSCLOUD_KEYWORDS = (
    "Sistema contable DS-CONT para Perú. "
    "Términos frecuentes: RUC, SUNAT, DNI, IGV, MYPE, régimen tributario, estados financieros"
    "plan contable general empresarial, libros electrónicos, PLE, PDT, "
    "asientos contables, amarres contables, asiento de apertura, cierre contable, "
    "hoja electrónica Excel, archivo XML, copia de seguridad, "
    "anticlick, clic derecho, menú lateral, plan de cuentas, "
    "comprobantes de pago, facturas, boletas, notas de crédito, notas de débito, "
    "registro de compras, registro de ventas, libro diario, libro mayor, "
    "balance general, estado de resultados, flujo de caja, DS-CONT Cloud"
    "régimen general, régimen especial, régimen MYPE tributario, RER, RUS, "
    "cronograma tipo A, cronograma tipo B, declaración mensual, declaración anual."
)

def transcribe(video_path, model_name="turbo"):
    import whisper

    print(f"\nTRANS: {video_path} with {model_name} model")
    print("-"*20)
    model = whisper.load_model(model_name)

    result = model.transcribe(video_path , initial_prompt=DSCLOUD_KEYWORDS)
    # result = {"text": <full_trans>, 
    #         "segments": {<timeN-timeN+1: <trans_within_times>,
    #                     <timeN+1-timeN+2: <trans_within_times> ...},
    #         "language": <string>}

    return result["text"]


# ----------------------------- DOWNLOAD


def download_video(url, video_path, video_format="mp3"):

    import os
    import yt_dlp

    print(f"\nDownloading {url}")
    print("="*40)
    
    # ---

    # set param
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": video_path,
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": video_format,
            "preferredquality": "192",
        }],
    }

    # download file
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        main = ydl.download([url])

    # 
    final_path = video_path + "." + video_format
    print(f">>>>> Download finished in {final_path}")
    
    return final_path



if __name__ == "__main__":
    string = "pipi tuvieras fe como un granito de mostaza eso dice el señor tu le dirias a las montañas muevanse"
    string2 = "xd tuvieras fe como un granito de mostaza eso dice el señor tu le dirias a las montañas muevanse"
    compare_two_strings(input1=string, input2=string2,words_number=9, padding=60)
