Challenge - Rev (Disciplina Segurança Cibernética - PPGCC UFSCar 2023) 
https://ctf.knping.pl/challenges#noodle-nightmare-6

![2023-12-14_21-42_1](https://github.com/stnert/cybersec-rev-pres/assets/48295298/9c2397f2-9507-412d-b67a-e1ee2f7863e2)



Esse problema fornece um arquivo noodleNightmare.cpp e uma pasta chamada spaghetti contando com mais de 100 arquivos onde cada um contém apenas um palavra ou operador. O arquivo principal é formado inteiramente por #include dos arquivos da pastas, então para conseguir ler esse programa devemos substituir esses includes pela respectiva palavra/operador. Por exemplo, logo no final do arquivo na linha 853 encontramos:
'''
#include "spaghetti/dhokpbpcvzqlsolslehczhyqudugoqczubzjshwlrvsmnnsbji.cpp"

#include "spaghetti/tcjbyqgtoylnpctxlgbcysapjpvqllgwzureosicdambypdocy.cpp"

#include "spaghetti/qxecmpoitqtpdyeumdbdfdyidxnbndzrnlviojinuqyxyglucp.cpp"

#include "spaghetti/nebwpbpbsokfblfcdoqptvnlakmjhnclhnqqplrsslbcomoxff.cpp"

#include "spaghetti/khgyjkyieeaomicojuzkewykloeooejjcauiubrljhpjiqrhjy.cpp"

#include "spaghetti/psotqgfoicptyfqggfkwhkjwyaqvmzmnbqjohnzwmghjnaxfve.cpp"

#include "spaghetti/znxmlwbedrctssyajamboadihyziwjpezyglhemygmjesdiycp.cpp"

#include "spaghetti/ekvebarjreidkaxcssntrzdwhvtzlfjgjszsoorotnrlrncqoa.cpp"

#include "spaghetti/fmcsuuahfryuftpsmdmyfttnnftyqjizlshaurgjlobhdxnlyi.cpp"

#include "spaghetti/nkkdzjjfvwopooqnlcivscopgvvyjvoixfpzpyajtwlxmszbcz.cpp"

#include "spaghetti/ayvgnofqweiesllskmpithbwgpzuekbthcbzmwuwfgbszwyscz.cpp"
;
#include "spaghetti/djoodumzqpuejednbfofcqohalvroroxsdeqpjtzywxopvodhx.cpp"

#include "spaghetti/gitqhgznnkvhcvwonsbljbwzfryfdjwrveupckassrafhuqudw.cpp"

#include "spaghetti/oqdoesjogfnmyorloreqdtljzzfaofqfexbqyhiishvujfmqbx.cpp"

#include "spaghetti/zzibjedgygsdnzkclvzmqyfqvaqozqpnutrefnlgmqvcmimlha.cpp"

#include "spaghetti/utvmyapvbtlkdnhqtdquzzfhcvylqifvbpnnkihdjxibxlqalw.cpp"

#include "spaghetti/ysdhhqwvzmrgwlgzoomxnbhofswnshmaxtivntzyhglvcwgfsn.cpp"

#include "spaghetti/tzcyzmfzgpwlmmwzjyztyedvtjwnafjcoebiqpllbkcgqrtlku.cpp"

#include "spaghetti/odpeswpyfiutfonuaxezaffpnvcsiualbyjpszbatalvtztiwu.cpp"
;
#include "spaghetti/gjzmlkoxjnastqhmykroyvvycsvujbspjbojqyydkfampwrujw.cpp"

#include "spaghetti/xhfvwsawrgulvmvkkxnjknpngavtbmikgmbmlbdtekqcioyyey.cpp"
'''
Substituindo os includes encontramos:
'''
if

____

==

__

)

{

cout

<<

"Congratulations, you have untangled this spaghetti!"

<<

endl
;
}

else

{

cout

<<

"Not this time!"

<<

endl
;
}

}
'''

A partir disso podemos concluir que ____ ou __ é a nossa flag, então é necessário incluir a impressão dessas variáveis:
'''
cout << ____ << endl;
cout << __ << endl;
'''
Onde obtemos nossa flag:
![image](https://github.com/stnert/cybersec-rev-pres/assets/91509232/5299519b-0dc6-4bd7-8325-6db9daf1e43b)
