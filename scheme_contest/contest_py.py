import sys
sys.setrecursionlimit(10000000)

class Compl :
    def __init__ (self, real, imag) :
        self.real = real
        self.imag = imag
    def __repr__ (self) :
        return "("+str(self.real)+" "+str(self.imag)+")"

def cmul (c1, c2) :
    return Compl((c1.real*c2.real-c1.imag*c2.imag), (c1.real*c2.imag + c2.real*c1.imag))

def csq (c) :
    return cmul(c, c)

def cadd (c1, c2) :
    return Compl((c1.real+c2.real), (c1.imag+c2.imag))

def out_of_bounds (c) :
    if (c.real*c.real + c.imag*c.imag) > 4 :
        return True
    else :
        return False

max_iters = 1024
def orbitof (c) :
    lst = [c]
    def help( z, iters) :
        if iters == max_iters or out_of_bounds(z):
            return None
        else: 
            next_z = cadd(csq(z), c)
            lst.append( next_z )
            help( next_z, iters+1)
    help( Compl(0, 0), 0)
    return lst

def getorbits(inputs) :
    lst = []
    for c in inputs :
        lst.append(orbitof(c))
    return lst
px = 5
pixelsize = 1/500*px
def in_square (orbit, x, y) :
    count = 0
    for c in orbit :
        if (c.real > x and c.real < x +pixelsize and c.imag > y and c.imag < y +pixelsize) :
            count+= 1
    return count 

def num_thru_square (orbits, x, y) :
    count = 0
    for orbit in orbits :
        count += in_square(orbit, x, y)
    return count

def rgb_hex (num) :
    num *= 10
    if num>255:
        num = 255
    return '#%02x%02x%02x' % (num, num, num)

inputs = [[0.1063477849698022,0.6259995079328755],[0.38588203467186544,-0.17805849588853],[-1.2587455529437832,0.036971099936866696],[-0.5423338650347062,0.5427980878973028],[-0.21059614271601457,0.6927333745979815],[-0.22891082252383066,-0.7434798702851638],[-1.174711906425048,0.24654796804988555],[-1.2466373875517764,0.0870398209916836],[-0.5232951446885994,0.5262621364855082],[-0.5751137630543747,-0.5419276441565367],[0.19376376958128852,-0.558888883568764],[-1.232080918377313,0.1225168409712959],[-0.8893055145196535,-0.22855146370581605],[-0.40418167405253136,0.5929098954592811],[-1.2730575805525834,-0.05262016689007312],[-0.2111956685790341,-0.6440439452891952],[-0.15825570448686233,-0.8404981965955086],[-0.22873114405012082,-0.7437037378070539],[-0.7593270285722331,-0.07103760864333494],[-0.21341374698041712,-0.7929573980203964],[-1.14552857274046,-0.21203497253422757],[-0.017702618580807752,0.6441580986379779],[-1.3672716107432914,-0.03443937797020626],[0.3690894742998263,0.10580595033347262],[-1.2860607756463245,0.05472951149223637],[-0.7279152972482008,-0.1952638419617793],[0.36820063867726144,0.10586615456725897],[-0.24606932996439895,0.7580440310947352],[-0.17601672649223823,0.6611766622722745],[-0.6920546478365922,-0.3707484320864105],[0.37021522440254206,-0.5936583709182989],[-0.6253123542811174,0.40317786016173307],[0.14174502160514957,-0.6103102392671957],[-0.542856113536142,-0.5917582170004216],[-1.1186278320735663,-0.26326923099245986],[-0.06929031243595642,-0.8242369704835132],[-1.391337616740479,-0.01631602850208591],[-0.5760375733499883,-0.5745940609573207],[-0.5578468368419144,-0.6267438319505215],[-0.7430321028164721,-0.1605994817149329],[-1.1619094678449837,0.19328372313755246],[-1.1325134424951162,-0.21329385761321118],[-1.0421759390045935,0.2472658982853719],[-0.17703763443623138,-0.8561474030302187],[-0.6755887457983579,-0.45592841703921183],[0.2135336355719221,0.5427400617652326],[-0.7262865580803001,-0.17787834725766655],[-0.3004696923720396,-0.6594694228191598],[-0.9524259857299887,0.24678728171755948],[-0.1235398080145244,-0.83923974514271],[-0.8548395259721331,-0.2129341848617453],[-0.30035048292547034,0.6584448201827886],[0.14228625031498734,-0.6094489804713039],[0.315697579719134,-0.4914975131609299],[0.37098540452237033,-0.2821803306242197],[-0.9815704685103546,0.26350828544903576],[-0.9657913238941811,-0.24852219828723765],[0.333760346833827,0.3884254136364585],[-0.3702744710470992,0.642959371780778],[0.26571935710006056,-0.5759221043867195],[-0.5409410073162427,0.5425079523056977],[-0.8730347169909026,0.23082727613146017],[-0.6590709892928033,-0.422033593282675],[-0.035946362241334996,-0.709594890785085],[-1.2726855607994116,-0.052981773046891875],[-1.146072128278653,-0.28241907106726316],[0.3358406758130304,0.4042997628313072],[0.36897096723952255,-0.28194158607858105],[-0.3867693337455536,0.6257704658125348],[-0.035223012286277486,-0.6931858087531064],[-0.37033371735519455,0.6424455527979498],[-0.7097639874310477,0.3537534865412553],[-1.453829658970603,-0.0006631757618564277],[-1.2472030319831118,-0.07091710718421036],[-0.10472225773771106,0.9353304593260242],[-0.3683784118299813,0.6430164598583336],[-0.3518545019245609,-0.6592986691880321],[-1.21909196018644,-0.12335928676843197],[-0.30005245453384094,-0.6596401710570553],[-1.3132003444782012,-0.0717003620414088],[-0.5413472867633843,0.5407088368170473],[0.35327877117720785,0.43920342615521163],[-0.10526410790948179,0.8883333696600184],[0.28080749356738854,0.5751715051195471],[0.2815237732622842,0.4730299011702313],[-0.5262621364855082,-0.508288154761845],[0.01927005795330511,0.6437014711989587],[-0.7108347980038854,-0.22897071493245885],[-0.6768369856588892,0.35327877117720785],[-0.45616321882705574,0.5942340592410358],[-0.5750560204666069,0.45768926863764114],[-1.3150182727591284,-0.0691095546108894],[-0.6923940225422751,-0.3700967301042579],[0.12215578608404336,-0.5923340831420184],[0.3529227211699033,0.4223871732891309],[-1.0289393442620969,0.28158346157535025],[-0.6431306342605002,0.420265486394795],[-1.1333580525878935,0.21203497253422757],[-1.059137223513944,-0.26410590482170543],[-0.29909871790840975,-0.6425597388819166],[0.19484383283686568,0.558888883568764],[-1.059137223513944,0.26356804846470233],[-0.2649425316132464,0.6438156315692706],[0.3184357880451476,0.45616321882705574],[-1.2447979169668468,0.0546089791338282],[0.3335820156014083,-0.40317786016173307],[0.0895092489448939,-0.6085301670854236],[-0.2110158128327015,0.6438156315692706],[-0.6776878876537361,0.31665006912323823],[-0.7430321028164721,-0.12474325709777696],[-1.3404583516867494,-0.06947106969435768],[0.315697579719134,-0.49196501779801066],[-0.14252679304899954,-0.8574003647293239],[-0.45557620192969395,-0.5773653158344426],[-0.22938995596408446,0.8566922195895228],[-0.2822997013587828,-0.6425026461318485],[-0.26464374173965693,0.6446717597274327],[0.21143547355382072,0.5432622791931236],[-1.2452225629732931,-0.17835874036993712],[-1.273336546782854,-0.051535338138893286],[-0.19562384286396553,0.8095089067887999],[0.12305841578378629,-0.5937735129000938],[-0.0870398209916836,0.8722210052959244],[0.38854369448255455,-0.14246665755962717],[0.37116313030989695,-0.08908764886905968],[-1.2596355072176184,0.03703137832511354],[0.29832375565844543,-0.45727843669119256],[-0.5578468368419144,0.593428080481767],[0.35096424007510624,-0.5092210429605659],[-0.17661726619214296,0.8255001821783612],[0.10556513243743462,-0.6264575648661703],[0.3334631265974392,-0.05219829086569932],[-0.7100458022746403,-0.2470265917972147],[-0.15795520434031973,-0.8400605201449705],[-0.5258549758034907,-0.506888600832879],[-0.06989283441862332,-0.8231382034532069],[-1.1458250731971098,0.21329385761321118],[-0.9508882256800689,0.24804361952604975],[-1.2448922906650361,0.07001333805478432],[0.3010657232143354,0.4916143920009519],[-1.2463073529644162,-0.08746144015832989],[-0.3525666596175955,-0.6585586744987524],[-0.49167283075090773,-0.5254477917075596],[-1.14552857274046,-0.28343367209994735],[-0.26440470551187334,0.6445576169179453],[-0.6764965861043422,0.44049730426884615],[0.3707484320864105,0.15765470060550077],[-0.49173126905408926,0.6088747387054221],[-0.6439297895994878,0.4054215328767291],[0.40506730405462654,0.33304700554150674],[-1.0286808421608216,-0.2644644649293447],[-0.7578208638849782,-0.07025434456323001],[-0.4219157302119971,0.593485653899887],[-0.6261712835505506,-0.4031188089859839],[-0.6590709892928033,-0.42167999947042273],[-1.0589837964026783,-0.26571935710006056],[-0.47285416467679575,0.6273163233994065],[0.40483114414429516,-0.33459252313765087],[0.36944498742977516,0.2815237732622842],[-0.19604383582761503,0.8066963454695112],[-0.5602201482260559,-0.5588309963978517],[-1.2465430976187302,-0.06989283441862332],[-0.37021522440254206,-0.642160077372813],[-0.7271852415094535,0.17595667164165957],[-0.03455993744300719,-0.6930727039926105],[-0.9666359073359254,0.2481632655697906],[0.40288260062045556,-0.36867469372235284],[-0.5401864244560541,-0.5914126715015517],[-0.7276906766139808,0.21035632700953785],[0.3175429610455707,0.4914390730709699],[0.28337399174406563,-0.4732056337951629],[0.40418167405253136,0.14288760326357888],[-1.217801120830941,-0.1235398080145244],[-0.36867469372235284,-0.6437585516766006],[-0.7261180361220689,-0.19334372955830906],[0.26470350019554606,0.48904264550252685],[0.31581664491535316,-0.5773653158344426],[-0.2990391070568404,0.6434731434397102],[0.1763770522349924,0.5912398914964282],[-0.7257247951285475,0.19520384119008227],[-1.366567450071047,-0.03630803546093346],[-0.26380709813183023,0.6416461848502073],[-0.5065386708679707,-0.6081281417031839],[-0.50607207180758,-0.6105398872127406],[-0.6589571457516662,-0.43849759300488644],[-0.6766100550819557,-0.43879169712911614],[-0.5253314490964588,0.5234115206537892],[-0.7269605865027233,0.24834273294400477],[0.10484266955451226,0.6422742692937888],[-0.5239933719344,0.5234697079229886],[-0.7092566800850469,-0.247146245490448],[-0.7274098859437009,0.21173522544902412],[0.10496308099023886,0.6431877205850076],[-0.2995755949321321,0.643872710876917],[-0.49132219155141743,-0.6253123542811174],[-0.7255000714803014,-0.19442381503644868],[-0.7110038520510513,-0.2288509299071953],[-0.856365338992302,-0.23046795738665474],[-1.1474057756854266,0.21185512486068678],[-0.9196999107136248,-0.28098656693949753]]
for i in range(len(inputs)) :
    inputs[i] = Compl(inputs[i][0], inputs[i][1])

os = getorbits(inputs)

import pygame as pygame
pygame.init()                                       # start up pygame
size = 500                                         # set size of grid (size x size)
display = pygame.display.set_mode((size,size))      # create display of size as indicated above
pygame.display.update()                             # start the display
pygame.display.set_caption('buddhabrot')          # set the name of the window



screensize = int(size/px)
for n in range(screensize) :
    x =  (n-screensize/2)/(screensize/4)
    for m in range(screensize) :
        y = (m-screensize/2)/(screensize/4)
        num = (num_thru_square(os, x, y))
        num /= 10
        if num > 1 :
            num = 1
        num = 255*(1 - (1-num)**2)
        pygame.draw.rect(display, (num, num, num), [m*px, n*px, px, px])
        pygame.display.update()

        

close = False
while not close :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            close = True
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_r:
                close= True


pygame.quit()

        