from functions import *
import networkx as nx
from ipywidgets import *
from csv import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img_files = {'America/MG': 'Escudos\\americamg_bra.png',
             'AthleticoParanaense/PR': 'Escudos\\atleticopr_bra.png',
             'Atletico/GO': 'Escudos\\atleticogo_bra.png',
             'Atletico/MG': 'Escudos\\atleticomg_bra.png',
             'Avai/SC': 'Escudos\\avai_bra.png',
             'Bahia/BA': 'Escudos\\bahia.png',
             'Botafogo/RJ': 'Escudos\\botafogorj_bra.png',
             'CSA/AL': 'Escudos\\csa_bra.png',
             'Ceara/CE': 'Escudos\\ceara_bra.png',
             'Chapecoense/SC': 'Escudos\\chapecoense_bra.png',
             'Corinthians/SP': 'Escudos\\corinthians_bra.png',
             'Coritiba/PR': 'Escudos\\coritiba_bra.png',
             'Criciuma/SC': 'Escudos\\criciuma_bra.png',
             'Cruzeiro/MG': 'Escudos\\cruzeiro_bra.png',
             'Figueirense/SC': 'Escudos\\figueirense.png',
             'Flamengo/RJ': 'Escudos\\flarj.png',
             'Fluminense/RJ': 'Escudos\\flurj.png',
             'Fortaleza/CE': 'Escudos\\fortaleza.png',
             'Goias/GO': 'Escudos\\goias.png',
             'Gremio/RS': 'Escudos\\gremio.png',
             'Internacional/RS': 'Escudos\\internacional_bra.png',
             'Joinville/SC': 'Escudos\\joinville.png',
             'Nautico/PE': 'Escudos\\nautico.png',
             'Palmeiras/SP': 'Escudos\\palmeiras.png',
             'Parana/PR': 'Escudos\\parana.png',
             'PontePreta/SP': 'Escudos\\pontepreta_bra.png',
             'Portuguesa/SP': 'Escudos\\portuguesasp_bra.png',
             'RedBullBragantino/SP': 'Escudos\\bragantino_bra.png',
             'SantaCruz/PE': 'Escudos\\santa.png',
             'Santos/SP': 'Escudos\\santos.png',
             'SaoPaulo/SP': 'Escudos\\saopaulo_bra.png',
             'Sport/PE': 'Escudos\\sport.png',
             'Tubarao/SC': 'Escudos\\atleticotubarao_sc.png',
             'VascodaGama/RJ': 'Escudos\\vasco.png',
             'Vitoria/BA': 'Escudos\\vitoria.png',
             'ABC/RN': 'Escudos\\abcrn_bra.png',
             'ASA/AL': 'Escudos\\asaarapiracaal_bra.png',
             'America/RN': 'Escudos\\americarn.png',
             'Boa/MG': 'Escudos\\boa_mg.png',
             'Botafogo/PB': 'Escudos\\botafogopb_bra.png',
             'Botafogo/SP': 'Escudos\\botafogosp_bra.png',
             'Brasil/RS': 'Escudos\\brasilpelotas_bra.png',
             'CRB/AL': 'Escudos\\crb_bra.png',
             'Caldense/MG': 'Escudos//caldense.png',
             'Campinense/PB': 'Escudos\\campinensepb_bra.png',
             'Caxias/RS': 'Escudos\\caxias.png',
             'Central/PE': 'Escudos//centralpe.png',
             'Confianca/SE': 'Escudos\\confianca_se.png',
             'Cuiaba/MT': 'Escudos\\cuiaba_bra.png',
             'Guarani/SP': 'Escudos\\guaranisp_bra.png',
             'Guaratingueta/SP': 'Escudos\\guaratinguetasp_bra.png',
             'Icasa/CE': 'Escudos\\icasa_ce.png',
             'Juventude/RS': 'Escudos\\juventude.png',
             'Londrina/PR': 'Escudos\\londrina_pr.png',
             'Luverdense/MT': 'Escudos\\luverdensemt_bra.png',
             'Macae/RJ': 'Escudos\\macaerj_bra.png',
             'MogiMirim/SP': 'Escudos\\mogimirim_sp.png',
             'MotoClub/MA': 'Escudos\\motoclubma_bra.png',
             'Oeste/SP': 'Escudos\\oestesp_bra.png',
             'Operario/PR': 'Escudos\\operario_pr.png',
             'Paysandu/PA': 'Escudos\\paysandu.png',
             'Remo/PA': 'Escudos\\remo.png',
             'RioBranco/AC': 'Escudos\\riobranco_ac.png',
             'River/PI': 'Escudos\\riverpi_bra.png',
             'Salgueiro/PE': 'Escudos\\salgueirope_bra.png',
             'SampaioCorrea/MA': 'Escudos\\samapaiocorrea_ma.png',
             'Santos/AP': 'Escudos\\ap_santos.png',
             'SaoBento/SP': 'Escudos\\saobento_bra.png',
             'SaoCaetano/SP': 'Escudos\\saocaetano_bra.png',
             'Tombense/MG': 'Escudos\\tombense_mg.png',
             'Treze/PB': 'Escudos\\trezepb_bra.png',
             'Tupi/MG': 'Escudos\\tupijf_bra.png',
             'VilaNova/GO': 'Escudos\\vilago.png',
             'VillaNova/MG': 'Escudos\\villanovamg.png',
             'Ypiranga/RS': 'Escudos\\ypiranga_rs.png',
             'Aguia/PA': 'Escudos\\aguiamaraba.png',
             'Atletico/AC': 'Escudos\\atleticoac.png',
             'Baraunas/RN': 'Escudos\\baraunas.png',
             'Brasiliense/DF': 'Escudos\\brasiliense.png',
             'Brusque/SC': 'Escudos\\brusque.png',
             'DuquedeCaxias/RJ': 'Escudos\\duque_caxias.png',
             'Ferroviario/CE': 'Escudos\\ferroviario.png',
             'Globo/RN': 'Escudos\\globo.png',
             'GremioBarueri/SP': 'Escudos\\gremiobarueri.png',
             'Imperatriz/MA': 'Escudos\\imperatriz.png',
             'Ituano/SP': 'Escudos\\ituanofc.png',
             'Jacuipense/BA': 'Escudos\\jacuipense.png',
             'Juazeirense/BA': 'Escudos\\juazeirense.png',
             'Madureira/RJ': 'Escudos\\madureira.png',
             'Manaus/AM': 'Escudos\\manausfc.png',
             'SaoJose/RS': 'Escudos\\saojose_rs.png',
             'VoltaRedonda/RJ': 'Escudos\\volta.png',
             'Afogados/PE': 'Escudos//afogados.png',
             'AguiaNegra/MS': 'Escudos//aguianegra.png',
             'Altos/PI': 'Escudos//altos.png',
             'Aparecidense/GO': 'Escudos//aparecidense.png',
             'Aquidauanense/MS': 'Escudos//aquidauanense.png',
             'AtleticodeCajazeiras/PB': 'Escudos//atleticocajazeiras.png',
             'BahiadeFeira/BA': 'Escudos//bahiafeira.png',
             'Bangu/RJ': 'Escudos//bangu.png',
             'Bare/RR': 'Escudos//bare.png',
             'Bragantino/PA': 'Escudos//bragantinopa.png',
             'Cabofriense/RJ': 'Escudos//cabofriense.png',
             'Coruripe/AL': 'Escudos//coruripeal.png',
             'FastClube/AM': 'Escudos//fastclub.png',
             'FcCascavel/PR': 'Escudos//cascavel.png',
             'Ferroviaria/SP': 'Escudos//ferroviariasp.png',
             'Floresta/CE': 'Escudos//floresta.png',
             'FreiPaulistano/SE': 'Escudos//freipaulistano.png',
             'Galvez/AC': 'Escudos//galvez.png',
             'Gama/DF': 'Escudos//gama.png',
             'Goianesia/GO': 'Escudos//goianesia.png',
             'Goiania/GO': 'Escudos//goiania.png',
             'GuaranideJuazeiro/CE': 'Escudos//guaranijuazeiro.png',
             'GuaranydeSobral/CE': 'Escudos//guaranysobral.png',
             'IndependenteTucurui/PA': 'Escudos//independentetucurui.png',
             'Ipatinga/MG': 'Escudos//ipatinga.png',
             'Itabaiana/SE': 'Escudos//itabaiana.png',
             'Jacioba/AL': 'Escudos//jacyoba.png',
             'Ji-parana/RO': 'Escudos//jiparana.png',
             'MarcilioDias/SC': 'Escudos//marciliodias.png',
             'Mirassol/SP': 'Escudos//mirassol.png',
             'Nacional/AM': 'Escudos//nacionalam.png',
             'Nacional/PR': 'Escudos//nacionalpr.png',
             'Novorizontino/SP': 'Escudos//novorizontino.png',
             'Operario/MT': 'Escudos//operariomt.png',
             'Palmas/TO': 'Escudos//palmasto.png',
             'Pelotas/RS': 'Escudos//pelotas.png',
             'Portuguesa/RJ': 'Escudos//portuguesarj.png',
             'Potiguar/RN': 'Escudos//potiguar.png',
             'RealNoroeste/ES': 'Escudos//realnoroeste.png',
             'SaoLuiz/RS': 'Escudos//saoluizrs.png',
             'SaoRaimundo/RR': 'Escudos//saoraimundorr.png',
             'Sinop/MT': 'Escudos//sinopmt.png',
             'SociedadeEsportivaJuventude/MA': 'Escudos//juventudema.png',
             'Tocantinopolis/TO': 'Escudos//tocantinopolis.png',
             'TocantinsEsporteClube/TO': 'Escudos//tocantinsec.png',
             'Toledo/PR': 'Escudos//toledo.png',
             'Tupynambas/MG': 'Escudos//tupynambas.png',
             'UniaodeRondonopolis/MT': 'Escudos//rondonopolis.png',
             'Vilhena/RO': 'Escudos//vilhena.png',
             'Vilhenense/RO': 'Escudos//vilhenense.png',
             'VitoriaF.C./ES': 'Escudos//vitoriaes.png',
             'VitoriadaConquista/BA': 'Escudos//vitoriaconquista.png',
             'Ypiranga/AP': 'Escudos//ypirangaap.png',
             '4deJulho/PI': 'Escudos\\4dejulho.png',
             '7deSetembro/MS': 'Escudos\\7desetembroms.png',
             'A.s.s.u./RN': 'Escudos\\assurn.png',
             'Aimore/RS': 'Escudos\\aimore.png',
             'Amadense/SE': 'Escudos\\amadense.png',
             'America/PE': 'Escudos\\americape.png',
             'Americano/RJ': 'Escudos\\americanorj.png',
             'Anapolina/GO': 'Escudos\\anapolina.png',
             'Anapolis/GO': 'Escudos\\anapolis.png',
             'Aracruz/ES': 'Escudos\\aracruz.png',
             'Araguaia/MT': 'Escudos\\araguaia.png',
             'ArapongasEsporteClube/PR': 'Escudos\\arapongas.png',
             'Araxa/MG': 'Escudos\\araxa.png',
             'AssociacaoDesportivaItaborai/RJ': 'Escudos\\itaboraifc.png',
             'Atletico/BA': 'Escudos\\atleticoba.png',
             'Atletico/ES': 'Escudos\\atleticoes.png',
             'Atletico/PE': 'Escudos\\atleticope.png',
             'AtleticoCearense/CE': 'Escudos\\atleticoce.png',
             'AtleticoPatrocinense/MG': 'Escudos\\patrocinense.png',
             'AtleticoRoraima/RR': 'Escudos\\atleticorr.png',
             'Audax/SP': 'Escudos\\audaxsp.png',
             'Avenida/RS': 'Escudos\\avenida.png',
             'Barbalha/CE': 'Escudos\\barbalha.png',
             'Barcelona/RO': 'Escudos\\barcelona.png',
             'BeloJardim/PE': 'Escudos\\belojardim.png',
             'Betim/MG': 'Escudos\\betim.png',
             'Boavista/RJ': 'Escudos\\boavistarj.png',
             'Brasilia/DF': 'Escudos\\brasilia.png',
             'Cameta/PA': 'Escudos\\cameta.png',
             'Capivariano/SP': 'Escudos\\capivariano.png',
             'Caucaia/CE': 'Escudos\\caucaia.png',
             'Ceilandia/DF': 'Escudos\\ceilandia.png',
             'Cene/MS': 'Escudos\\cene.png',
             'Cianorte/PR': 'Escudos\\cianorte.png',
             'ColoColo/BA': 'Escudos\\colocoloba.png',
             'Comercial/MS': 'Escudos\\comercialms.png',
             'Cordino/MA': 'Escudos\\cordinoma.png',
             'Corumbaense/MS': 'Escudos\\corumbaense.png',
             'Crac/GO': 'Escudos\\crac.png',
             'Desportiva/ES': 'Escudos\\desportiva.png',
             'DomBosco/MT': 'Escudos\\dombosco.png',
             'EspiritoSanto/ES': 'Escudos\\espiritosanto.png',
             'Estanciano/SE': 'Escudos\\estanciano.png',
             'EstreladoNorte/ES': 'Escudos\\estreladonorte.png',
             'Flamengo/PE': 'Escudos\\flamengope.png',
             'Flamengo/PI': 'Escudos\\flamengopi.png',
             'FluminensedeFeira/BA': 'Escudos\\fludefeira.png',
             'FozdoIguacu/PR': 'Escudos\\fozdoiguacu.png',
             'Friburguense/RJ': 'Escudos\\friburguense.png',
             'Galicia/BA': 'Escudos\\galicia.png',
             'Gaucho/RS': 'Escudos\\gaucho.png',
             'Genus/RO': 'Escudos\\genus.png',
             'Guarani/SC': 'Escudos\\guaranisc.png',
             'Gurupi/TO': 'Escudos\\gurupi.png',
             'HercilioLuzFutebolClube/SC': 'Escudos\\hercilioluz.png',
             'InterdeLages/SC': 'Escudos\\interdelages.png',
             'InterdeLimeira/SP': 'Escudos\\interdelimeira.png',
             'Interporto/TO': 'Escudos\\interporto.png',
             'Ipora/GO': 'Escudos\\ipora.png',
             'Itapora/MS': 'Escudos\\itapora.png',
             'Itumbiara/GO': 'Escudos\\itumbiara.png',
             'Ivinhema/MS': 'Escudos\\ivinhema.png',
             'J.Malucelli/PR': 'Escudos\\jmalucelli.png',
             'JacobinaEc/BA': 'Escudos\\jacobina.png',
             'Lagarto/SE': 'Escudos\\lagarto.png',
             'Lajeadense/RS': 'Escudos\\lajeadense.png',
             'Linense/SP': 'Escudos\\linense.png',
             'Luziania/DF': 'Escudos\\luziania.png',
             'Macapa/AP': 'Escudos\\macapa.png',
             'Maranhao/MA': 'Escudos\\maranhao.png',
             'Maringa/PR': 'Escudos\\maringa.png',
             'Metropolitano/SC': 'Escudos\\metropolitano.png',
             'Mixto/MT': 'Escudos\\mixto.png',
             'Murici/AL': 'Escudos\\murici.png',
             'Nautico/RR': 'Escudos\\nauticorr.png',
             'Naviraiense/MS': 'Escudos\\naviraiense.png',
             'Noroeste/SP': 'Escudos\\noroeste.png',
             'NovaIguacu/RJ': 'Escudos\\novaiguacu.png',
             'Novo/MS': 'Escudos\\novo.png',
             'NovoHamburgo/RS': 'Escudos\\novohamburgo.png',
             'Operario/MS': 'Escudos\\operario.png',
             'Oratorio/AP': 'Escudos\\oratorio.png',
             'Paragominas/PA': 'Escudos\\paragominas.png',
             'Parauapebas/PA': 'Escudos\\parauapebas.png',
             'Parnahyba/PI': 'Escudos\\parnahyba.png',
             'Penapolense/SP': 'Escudos\\penapolense.png',
             'Piaui/PI': 'Escudos\\piaui.png',
             'PlacidodeCastro/AC': 'Escudos\\placidodecastro.png',
             'Porto/PE': 'Escudos\\portope.png',
             'PrincesadoSolimoes/AM': 'Escudos\\princesadosolimoes.png',
             'Prudentopolis/PR': 'Escudos\\prudentopolis.png',
             'Pstc/PR': 'Escudos\\pstc.png',
             'RealDesportivo/RO': 'Escudos\\realdesportivo.png',
             'RedBullBrasil/SP': 'Escudos\\redbullbrasil.png',
             'Resende/RJ': 'Escudos\\resende.png',
             'RioBranco/ES': 'Escudos\\riobrancoes.png',
             'Rondoniense/RO': 'Escudos\\rondoniense.png',
             'S.francisco/PA': 'Escudos\\sfranciscopa.png',
             'SantaCruz/RN': 'Escudos\\santacruzrn.png',
             'SantaRita/AL': 'Escudos\\santaritaal.png',
             'SantoAndre/SP': 'Escudos\\santoandresp.png',
             'SaoBernardo/SP': 'Escudos\\saobernardosp.png',
             'SaoPaulo/RS': 'Escudos\\saopaulors.png',
             'SaoRaimundo/PA': 'Escudos\\saoraimundopa.png',
             'Sergipe/SE': 'Escudos\\sergipe.png',
             'Serra/ES': 'Escudos\\serra.png',
             'SerraTalhada/PE': 'Escudos\\serratalhada.png',
             'Serrano/BA': 'Escudos\\serranoba.png',
             'Serrano/PB': 'Escudos\\serranopb.png',
             'Sobradinho/DF': 'Escudos\\sobradinho.png',
             'Sousa/PB': 'Escudos\\sousa.png',
             'Sparta/TO': 'Escudos\\sparta.png',
             'Tiradentes/CE': 'Escudos\\tiradentes.png',
             'Trem/AP': 'Escudos\\trem.png',
             'Uberlandia/MG': 'Escudos\\uberlandia.png',
             'Urt/MG': 'Escudos\\urt.png',
             'Veranopolis/RS': 'Escudos\\veranopolis.png',
             'Vitoria/PE': 'Escudos\\vitoriape.png',
             'Votuporanguense/SP': 'Escudos\\votuporangense.png',
             'XvdePiracicaba/SP': 'Escudos\\xvdepiracicaba.png',
             'Ypiranga/PE': 'Escudos\\ypirangape.png'}

def change(string, old_char, new_char):
    new_string = ''
    for char in string:
        if char == old_char:
            new_string += new_char
        else:
            new_string += char
    return new_string

def replace(string):
    changes = [('á', 'a'), ('à', 'a'), ('â', 'a'), ('ã', 'a'),
               ('é', 'e'), ('ê', 'e'), ('í', 'i'), ('ó', 'o'),
               ('ô', 'o'), ('õ', 'o'), ('ú', 'u'), ('ç', 'c')]
    new_string = string
    for pair in changes:
        new_string = change(new_string, pair[0], pair[1])

    # abaixo uma gambiarra para evitar times duplicados
    if new_string == 'BOTAFOGO/RJ':
        new_string = 'Botafogo/RJ'
    elif new_string == 'Atletico/PR' or new_string == 'ATLETICO/PR':
        new_string = 'AthleticoParanaense/PR'
    elif new_string == 'A.b.c./' or new_string == 'A.b.c./RN' or new_string == 'Abc/RN':
        new_string = 'ABC/RN'
    elif new_string == 'A.s.a./' or new_string == 'A.s.a./AL' or new_string == 'Asa/AL':
        new_string = 'ASA/AL'
    elif new_string == 'America/' or new_string == 'AmericaFc/MG':
        new_string = 'America/MG'
    elif new_string == 'Guaratingueta/':
        new_string = 'Guaratingueta/SP'
    elif new_string == 'AMÉRICA/RN' or new_string == 'AmericadeNatal/RN':
        new_string = 'America/RN'
    elif new_string == 'AVAÍ/SC' or new_string == 'Avai/':
        new_string = 'Avai/SC'
    elif new_string == 'Arapongas/PR':
        new_string = 'ArapongasEsporteClube/PR'
    elif new_string == 'BOTAFOGO/PB':
        new_string = 'Botafogo/PB'
    elif new_string == 'Boa/':
        new_string = 'Boa/MG'
    elif new_string == 'Bragantino/' or new_string == 'Bragantino/SP':
        new_string = 'RedBullBragantino/SP'
    elif new_string == 'C.R.B./AL' or new_string == 'C.r.b./AL' or new_string == 'Crb/AL':
        new_string = 'CRB/AL'
    elif new_string == 'C.s.a./AL' or new_string == 'C.S.A./AL' or new_string == 'Csa/AL':
        new_string = 'CSA/AL'
    elif new_string == 'CAXIAS/RS' or new_string == 'SerCaxias/RS':
        new_string = 'Caxias/RS'
    elif new_string == 'CORITIBA/PR':
        new_string = 'Coritiba/PR'
    elif new_string == 'CRICIÚMA/SC':
        new_string = 'Criciuma/SC'
    elif new_string == 'Ceara/':
        new_string = 'Ceara/CE'
    elif new_string == 'Chapecoense/':
        new_string = 'Chapecoense/SC'
    elif new_string == 'Crac/GO':
        new_string = 'Chapecoense/SC'
    elif new_string == 'FIGUEIRENSE/SC' or new_string == 'Figueirense/':
        new_string = 'Figueirense/SC'
    elif new_string == 'FORTALEZA/CE':
        new_string = 'Fortaleza/CE'
    elif new_string == 'Guarany/CE':
        new_string = 'GuaranydeSobral/CE'
    elif new_string == 'Guarani/CE':
        new_string = 'GuaranideJuazeiro/CE'
    elif new_string == 'INDEPENDENTE/PA' or new_string == 'Independente/PA':
        new_string = 'IndependenteTucurui/PA'
    elif new_string == 'Icasa/':
        new_string = 'Icasa/CE'
    elif new_string == 'Internacional/SC':
        new_string = 'InterdeLages/SC'
    elif new_string == 'Joinville/':
        new_string = 'Joinville/SC'
    elif new_string == 'MURICI/AL' or new_string == 'MURICIFUTEBOLCLUBE/AL':
        new_string = 'Murici/AL'
    elif new_string == 'MaringaFutebolClube/PR':
        new_string = 'Maringa/PR'
    elif new_string == 'Novoperario/MS':
        new_string = 'Novo/MS'
    elif new_string == 'Oeste/':
        new_string = 'Oeste/SP'
    elif new_string == 'PIAUÍ/PI':
        new_string = 'Piaui/PI'
    elif new_string == 'PONTEPRETA/SP':
        new_string = 'PontePreta/SP'
    elif new_string == 'PalmasLtda/TO':
        new_string = 'Palmas/TO'
    elif new_string == 'Palmeiras/':
        new_string = 'Palmeiras/SP'
    elif new_string == 'Parana/':
        new_string = 'Parana/PR'
    elif new_string == 'Paysandu/':
        new_string = 'Paysandu/PA'
    elif new_string == 'REALNOROESTE/ES' or new_string == 'RealNoroesteCapixaba/ES' or new_string == 'RealNoroesteF.C./ES':
        new_string = 'RealNoroeste/ES'
    elif new_string == 'RiverA.c./PI' or new_string == 'RÍVER/PI':
        new_string = 'River/PI'
    elif new_string == 'SAMPAIOCORREA/MA':
        new_string = 'SampaioCorrea/MA'
    elif new_string == 'SANTOS/SP':
        new_string = 'Santos/SP'
    elif new_string == 'SantosFutebolClube/AP':
        new_string = 'Santos/AP'
    elif new_string == 'SaoCaetano/':
        new_string = 'SaoCaetano/SP'
    elif new_string == 'SerraF.C./ES':
        new_string = 'Serra/ES'
    elif new_string == 'Sobradinho(df)/DF':
        new_string = 'Sobradinho/DF'
    elif new_string == 'VillaNovaA.c./MG':
        new_string = 'VillaNova/MG'
    elif new_string == 'YpirangaRs/RS':
        new_string = 'Ypiranga/RS'
    elif new_string == 'ÁGUIANEGRA/MS' or new_string == 'ÁguiaNegra/MS':
        new_string = 'AguiaNegra/MS'
    elif new_string == 'ÁguiadeMaraba/PA' or new_string == 'AguiadeMaraba/PA' or new_string == 'Águia/PA':
        new_string = 'Aguia/PA'
    elif new_string == 'Uniao/MT':
        new_string = 'UniaodeRondonopolis/MT'
    elif new_string == 'Uniclinic/CE':
        new_string = 'AtleticoCearense/CE'
    
    return new_string

def preprocessing():
    players = [[year, ['ID', 'Team', 'Games', 'Competitions']] for year in range(2013, 2021)]
    index = [[year] for year in range(2013, 2021)]
    competitions = ['Serie A', 'Serie B', 'Serie C', 'Serie D', 'Copa do Brasil']
    clubs = []
    clubs_lower = []
    path = 'Participations and Goals/'
    
    for year in range(2013, 2021):
        for competition in competitions:
            for game in range(1, 601):
                try:
                    file = path + competition + '/' + str(year) + '/Game ' + str(game) + '.csv'
                    with open(file, mode = 'r') as list_of_players:
                        read = reader(list_of_players, delimiter = ',')
                        for line in read:
                            if line != ['CBF', 'Apelido', 'Nome', 'Nº', 'Clube']:
                                if line[0] != '' and line[0] != 'CBF':
                                    # I saw that some clubs, like Botafogo/RJ, have two diferents names:
                                    # Botafogo/RJ and BOTAFOGO/RJ, for example. So:
                                    if line[-1].lower() not in clubs_lower:
                                        clubs_lower.append(line[-1].lower())
                                        clubs.append(line[-1])

                                    ind = clubs_lower.index(line[-1].lower())
                                    team = replace(clubs[ind])
                            
                                    if [line[0], line[-1]] not in index[year - 2013]:
                                        index[year - 2013].append([line[0], team])
                                        players[year - 2013].append([line[0], team, 1, [competition]])
                                    else:
                                        ind = index[year - 2013].index([line[0], team])
                                        players[year - 2013][ind][2] += 1
                                        if competition not in players[year - 2013][ind][3]:
                                            players[year - 2013][ind][3].append(competition)
                except:
                    pass
    return players

def find_clubs(competitions, years):
    list_of_clubs = []
    for year in years:
        for competition in competitions:
            file = 'Participations and Goals/{}/{}/Index.csv'.format(competition, str(year))
            with open(file, mode = 'r') as index:
                read = reader(index, delimiter = ',')
                for line in read:
                    if line != ['Game', 'Home', 'Away']:
                        team1 = replace(line[1])
                        team2 = replace(line[2])
                        
                        if team1 not in list_of_clubs:
                            list_of_clubs.append(team1)
                        if team2 not in list_of_clubs:
                            list_of_clubs.append(team2)

    return list_of_clubs

def relations_one_club(team, players):
    athletes = []
    athletes_clubs = []
    clubs_lower = []

    for ind in range(len(players)):
        for player in players[ind]:
            if type(player) == list and player != ['ID', 'Team', 'Games', 'Competitions']:
                if team.lower() in player[1].lower() and player[0] not in athletes:
                    athletes.append(player[0])
                    athletes_clubs.append([player[0], team])
                    clubs_lower.append([team.lower()])

    for ind in range(len(players)):
        for player in players[ind]:
            if type(player) == list and player[0] in athletes:
                place = athletes.index(player[0])
                if player[1].lower() not in clubs_lower[place]:
                    clubs_lower[place].append(player[1].lower())
                    athletes_clubs[place].append(player[1])
            
    clubs = [[team, len(athletes)]]
    clubs_lower = [team.lower()]
    for element in athletes_clubs:
        for club in element:
            if not club.isdigit():
                if club.lower() not in clubs_lower and club != team:
                    clubs_lower.append(club.lower())
                    clubs.append([club, 1])
                elif club.lower() in clubs_lower and club != team:
                    ind = clubs_lower.index(club.lower())
                    clubs[ind][1] += 1
                
    clubs = sorted(clubs, key = lambda x : x[1], reverse = True)
    return clubs

def relations_list_of_clubs(list_of_clubs, players):
    relations = []
    for club in list_of_clubs:
        relations.append(relations_one_club(club, players))

    for club in relations:
        i = 1
        while i < len(club):
            if club[i][0] not in list_of_clubs:
                club.remove(club[i])
            else:
                i += 1
    
    return relations

def find_period(years):
    if len(years) == 1:
        return years[0]
    else:
        return 'the period from {} to {}'.format(years[0], years[-1])

def find_competitions(competitions):
    if len(competitions) == 1:
        return competitions[0]
    else:
        comp = competitions[0]
        for i in range(1, len(competitions)):
            if i == len(competitions) - 1:
                comp += ' and {}'.format(competitions[i])
            else:
                comp += ', {}'.format(competitions[i])
        return comp

def graph(relation, competitions, years, max_clubs):
    period = find_period(years)
    competitions = find_competitions(competitions)
    
    text = 'Below we can see what relationship exists between the players from {} clubs. Each node represents a club and an edge between\ntwo nodes represents that these clubs have players in commom (that is, players who have served in both clubs).\n\nThe bigger the node, the more players passed through the club.\nSimilarly, a thicker edge represents that the two clubs have more players in commom.\n\nHere we are looking at {} in {}.'.format(max_clubs, period, competitions)

    img_clubs = []
    col_clubs =[]
    for club in relation:
        if club[0][0] in img_files:
            img_clubs.append(club[0][0])
        else:
            col_clubs.append(club[0][0])
    
    G = nx.Graph()
    for club in relation:
        if club[0][0] in img_clubs and club[0][1] > 0:
            G.add_node(img_clubs.index(club[0][0]), color = 'white', weight = club[0][1])
        elif club[0][1] > 0:
            G.add_node(club[0][0], color = 'steelblue', weight = club[0][1])

    for club in relation:
        for i in range(1, len(club)):
            if club[0][0] in img_clubs:
                team_A = img_clubs.index(club[0][0])
            elif club[0][0] in col_clubs:
                team_A = club[0][0]

            if club[i][0] in img_clubs:
                team_B = img_clubs.index(club[i][0])
                G.add_edge(team_A, team_B, color = 'lightskyblue', width = club[i][1])
            elif club[i][0] in col_clubs:
                team_B = club[i][0]
                G.add_edge(team_A, team_B, color = 'lightskyblue', width = club[i][1])

    fig, ax = plt.subplots(figsize = (20, 20))
    pos = nx.spring_layout(G, scale = 1)
    nx.draw_networkx_edge_labels(G,
                                 pos,
                                 edge_labels = nx.get_edge_attributes(G, 'relation'),
                                 label_pos = 1.5,
                                 font_size = 9,
                                 font_color = 'red',
                                 font_family = 'sans-serif',
                                 font_weight = 'normal',
                                 alpha = 1.0,
                                 bbox = None,
                                 ax = ax,
                                 rotate = True)

    nx.draw_networkx(G,
                     pos = pos,
                     ax = ax,
                     node_color = [nx.get_node_attributes(G, 'color')[g] for g in G.nodes()],
                     edge_color = [nx.get_edge_attributes(G, 'color')[g] for g in G.edges()],
                     node_size = [nx.get_node_attributes(G, 'weight')[g] * 10 for g in G.nodes()],
                     width = [nx.get_edge_attributes(G, 'width')[g] * 0.5 for g in G.edges])

    labels = {}
    for g in G.nodes():
        labels[g] = g

    nx.draw_networkx_labels(G,
                            pos = pos,
                            labels = labels,
                            ax = ax,
                            font_color = 'white')

    print(text)
    trans = ax.transData.transform
    trans2 = fig.transFigure.inverted().transform
    weights = nx.get_node_attributes(G, 'weight')
    w_max = 0
    w_min = 1000
    for club in weights:
        if weights[club] > w_max:
            w_max = weights[club]
        if weights[club] < w_min:
            w_min = weights[club]

    dif = w_max - w_min
    new = 0
    relabel = {}
    
    for g in G.nodes():
        if type(g) == int:
            club = img_clubs[g]
            img = mpimg.imread(img_files[club])
            weight = nx.get_node_attributes(G, 'weight')[g]
            # option A (great)
            imsize = (weight - w_min)/dif * 0.04 + 0.02
            # option B (reasonable)
            imsize = weight/w_max * 0.05
            # option C (terrible)
            # imsize = weight/w_min * 0.03
            
            (x, y) = pos[g]
            xx, yy = trans((x, y))
            xa, ya = trans2((xx, yy))
            a = plt.axes([xa - imsize/2.0, ya - imsize/2.0, imsize, imsize])
            a.imshow(img)
            a.set_aspect('equal')
            a.axis('off')
            relabel[g] = new
            new += 1

    nx.relabel_nodes(G, relabel, copy = False)
                
    plt.show()
    return G, pos, ax, fig
