"""
💍 NEXT DIGITAL — Proyecto BODA
   Cliente: Natalia & Guille
   Ticket:  BODA-1 (P0, bloqueante)

DESCRIPCIÓN DE LA INCIDENCIA:
  El sistema que gestiona vuestra boda ha salido a producción sin pasar QA.
  La boda es en un mes, los tests están en rojo y el sobre sigue cerrado.
  El Account Manager dice que "es un cambio pequeñito".

INSTRUCCIONES:
  1. Ejecutad:  python boda.py
  2. Arreglad las funciones de la ZONA DE TRABAJO hasta que todo esté en verde.
  3. NO abráis el sobre hasta que el sistema os lo diga.
  4. No toquéis la sección "NO TOCAR". Está validada por el cliente.

Reglas: sin internet, sin IA, sin pedir ayuda al equipo. Solo vosotros dos y Python.
Estas horas no se imputan.
"""

NOVIA = "Natalia"
NOVIO = "Guille"


# ============================================================================
#  🛠️  ZONA DE TRABAJO — aquí sí podéis tocar
# ============================================================================


def limpiar_invitados(invitados):
    """
    El Excel de invitados lo exportó un consultor un viernes a las 18:59.

    Devuelve la lista sin duplicados, sin espacios de más, con cada nombre
    en formato Título ("celia" -> "Celia") y ordenada con sorted() de toda
    la vida (sí, Carlos sale el primero, que no se le suba).
    """
    return invitados  # TODO: lo limpiamos en la fase 2 del proyecto


ALIANZA = {"Iberia", "British Airways", "American Airlines", "Qatar Airways", "Finnair", "Japan Airlines"}


def luna_de_miel(vuelos):
    """
    Destino: Brasil (hay que conocer a la familia de Guille).

    Devuelve el vuelo más barato que cumpla TODO esto:
      - aerolínea de la ALIANZA (Natalia se ha pasado años en el proceso de
        Alianzas de Iberia, no vamos a volar con cualquiera)
      - destino en Brasil: "GRU" (São Paulo) o "GIG" (Río)
      - sin escalas (nada de escala en Daimiel)
    """
    return vuelos[0]  # el primero que salga, que estamos a fin de mes


DICCIONARIO = {
    "olá": "ea",
    "menino": "zagal",
    "menina": "zagala",
    "legal": "apañao",
    "obrigado": "gracias",
}


def traducir(frase):
    """
    La familia de Guille y la familia de Natalia van a compartir mesa.

    Traduce del brasileño al manchego de Daimiel usando DICCIONARIO,
    palabra a palabra. Lo que no esté en el diccionario se queda igual,
    y la puntuación también.
    """
    return frase  # TODO: pedir presupuesto a un traductor jurado


def repartir_premios(premios, gatos):
    """
    Los gatos han venido a la boda y exigen sus premios.

    Reparte los premios a partes iguales (enteros, que un gato no acepta
    medio premio). Devuelve una tupla (premios_por_gato, sobras).
    Las sobras son para los novios. No preguntéis.
    """
    return premios / gatos, 0  # las sobras se las queda el catering


def respuesta_valida(respuesta):
    """
    El cura necesita validar la respuesta en el altar.

    Tiene que aceptar "sí quiero" lo escribas como lo escribas: mayúsculas,
    sin tilde, con comas, con exclamaciones de emoción...
    Y también en portugués ("sim, quero"), por la familia de Guille.
    Pero ni "LGTM" ni "miau" valen como respuesta.

    Pista: el módulo unicodedata existe.
    """
    return respuesta == "Sí quiero"


def es_compatible(persona_a, persona_b):
    # Legacy. Heredado del proveedor anterior. Nadie se atreve a tocarlo.
    # Debería devolver True solo para la pareja de novios (en cualquier orden).
    if persona_a == persona_b:
        return True
    return False


# ============================================================================
#  🚫  NO TOCAR — tests de aceptación validados por el cliente
# ============================================================================


def test_invitados():
    excel = ["  laura", "Martina", "LAURA", "celia ", "Sergio", "ruth", "Álvaro", "laura  ", "CARLOS", "martina"]
    res = limpiar_invitados(excel)
    assert res.count("Laura") == 1, "Laura sale varias veces. Laura solo hay una."
    assert res == ["Carlos", "Celia", "Laura", "Martina", "Ruth", "Sergio", "Álvaro"], f"El Excel sigue mal: {res}"


def test_luna_de_miel():
    vuelos = [
        {"aerolinea": "Iberia", "destino": "GRU", "escalas": 1, "precio": 600},
        {"aerolinea": "Ryanair", "destino": "GRU", "escalas": 4, "precio": 49},
        {"aerolinea": "Iberia", "destino": "GRU", "escalas": 0, "precio": 950},
        {"aerolinea": "Iberia", "destino": "CDG", "escalas": 0, "precio": 120},
        {"aerolinea": "Iberia", "destino": "GIG", "escalas": 0, "precio": 890},
        {"aerolinea": "LATAM", "destino": "GRU", "escalas": 0, "precio": 700},
        {"aerolinea": "British Airways", "destino": "GIG", "escalas": 0, "precio": 870},
    ]
    v = luna_de_miel(vuelos)
    assert v["aerolinea"] != "Ryanair", "¿Ryanair? ¿Después de todo lo que hemos hecho por Iberia?"
    assert v["aerolinea"] != "LATAM", "LATAM se fue de oneworld en 2020. Natalia lo sabe mejor que nadie."
    assert v["aerolinea"] in ALIANZA, "Esa aerolínea no es de la alianza."
    assert v["destino"] in ("GRU", "GIG"), "Eso no es Brasil. Eso es París."
    assert v["escalas"] == 0, "Con escalas no. Es una luna de miel, no un Interrail."
    assert v["precio"] == 870,"Hay un vuelo más barato. El de compras no está contento."


def test_traducir():
    assert traducir("olá menino, a festa está muito legal!") == "ea zagal, a festa está muito apañao!", \
        "La abuela de Daimiel no ha entendido nada."
    assert traducir("obrigado menina") == "gracias zagala", "Malentendido diplomático entre familias."


def test_premios_gatos():
    assert repartir_premios(100, 3) == (33, 1), "Un gato se ha quedado sin premio. Ya está mirando los cables."
    assert repartir_premios(10, 2) == (5, 0), "Los gatos saben contar. Los gatos lo saben todo."


def test_si_quiero():
    for ok in ["Sí quiero", "si quiero", "SÍ, QUIERO", "Sí quiero!!!", "  sí  quiero  ", "Sim, quero"]:
        assert respuesta_valida(ok), f"El cura no acepta {ok!r}. La boda se ha parado."
    for ko in ["LGTM", "miau", "works on my machine", "lo imputo el viernes", "quiero"]:
        assert not respuesta_valida(ko), f"El cura ha aceptado {ko!r}. Eso no es un sí."


def test_compatibilidad():
    assert es_compatible(NOVIA, NOVIO), "El sistema dice que no sois compatibles. El sistema está mal."
    assert es_compatible(NOVIO, NOVIA), "El amor es conmutativo."
    assert not es_compatible(NOVIO, "Su ex"), "Ni de broma."
    assert not es_compatible(NOVIA, "Imputar horas el viernes"), "Nadie es compatible con eso."
    assert not es_compatible(NOVIA, NOVIA), "El amor propio está bien, pero no cuenta."


_SOBRE = (
    "wqFUZXN0cyBlbiB2ZXJkZSEg8J+OiQoKQk9EQS0xIOKGkiBEb25lLiBDbGllbnRlIHNhdGlzZmVjaG8uIENlcm8gaG9yYXMgZXh0"
    "cmEgKHBvciB1bmEgdmV6KS4KCk5hdGFsaWEgeSBHdWlsbGU6CmVsIGPDs2RpZ28gZXN0w6EgbGlzdG8gcGFyYSBwcm9kdWNjacOz"
    "biwKeSB2b3NvdHJvcyBwYXJhIGVsIG1hdHJpbW9uaW8uCgpRdWUgZXN0ZSBtZXJnZSBzZWEgcGFyYSBzaWVtcHJlLApzaW4gY29u"
    "ZmxpY3RvcyAobyBjb24gcG9jb3MsIHkgYmllbiByZXN1ZWx0b3MpLgoK8J+SjCAgWWEgcG9kw6lpcyBhYnJpciBlbCBzb2JyZS4g"
    "IPCfkowKClF1ZSBzZcOhaXMgbXV5IGZlbGljZXMganVudG9zLiDwn5Cx8J+QseKdpO+4jwoK4oCUIE1hcnRpbmEgeSBDYXJsb3Ms"
    "IENlbGlhIHkgU2VyZ2lv"
)

if __name__ == "__main__":
    import base64

    tests = [test_invitados, test_luna_de_miel, test_traducir, test_premios_gatos, test_si_quiero, test_compatibilidad]
    verdes = 0
    for t in tests:
        try:
            t()
            print(f"✅ {t.__name__}")
            verdes += 1
        except Exception as e:
            print(f"❌ {t.__name__}: {e or type(e).__name__}")

    print(f"\n{verdes}/{len(tests)} tests en verde.")
    if verdes == len(tests):
        print("\n" + "=" * 60)
        print(base64.b64decode(_SOBRE).decode())
        print("=" * 60)
    else:
        print("BODA-1 sigue en In Progress. El sobre sigue cerrado. 🔒")
