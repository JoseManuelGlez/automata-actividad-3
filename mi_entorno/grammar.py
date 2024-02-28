grammar = """
        start: s
                    
        s: v d
            | u f
            | i c 
            | o m
            | h w
            |

        v: "var"
        u: "func"
        i: "if"
        o: "void"
        h: "while"

        d: var_componente2 var_componente3
        var_componente2: con_nombrevar
        var_componente3: "=" numero_2 numeroa
        numero_2: "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
        numeroa: numero_2 numeroa | s |

        f: func_componente2 func_componente3 func_componente4 func_componente5 func_componente6 s
        func_componente2: letra func_rnombre | letramayuscula func_rnombre
        func_rnombre: letra func_rnombre | letramayuscula | numero func_rnombre |
        func_componente3: "(" ")"
        func_componente4: "{"
        func_componente5: v d |
        func_componente6: "}" 

        c: con_componente2 con_componente3 con_componente4 con_componente5 
        con_componente2: con_p_inicio con_logica
        con_componente3: "{"
        con_componente4: v d |
        con_componente5: func_componente6 con_componente7 | func_componente6 s
        con_componente7: e x
        con_componente10: func_componente6 s
        con_p_inicio: "("
        con_p_cierre: ")"
        e: "else"
        x: con_componente3 contenido_else
        contenido_else: con_componente4 con_componente10
        con_logica: con_nombreandop con_comparar
        con_nombreandop: con_nombrevar con_operador
        con_nombrevar: letra con_rnombre | letramayuscula con_rnombre
        con_rnombre: con_nombrevar | numero con_rnombre |
        con_operador: ">" | "<" | "==" | "<=" | ">=" | "!="
        con_comparar: numeroprueba con_p_cierre
        numeroprueba: numero_2 numeroa

        m: main_componente2 main_componente3 main_componente4 main_componente5 main_componente6 s
        main_componente2: "main"
        main_componente3: "(" ")"
        main_componente4: "{"
        main_componente5: v d |
        main_componente6: "}" 

        w: while_componente2 while_componente3 while_componente4 while_componente5 s
        while_componente2: while_pinicioandbandera con_p_cierre
        while_pinicioandbandera: "(" while_bandera
        while_componente3: "{"
        while_componente4: v d |
        while_componente5: "}" 
        while_bandera: "true" | "false"

        letra: "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j" | "k" | "l" | "m"
                    | "n" | "o" | "p" | "q" | "r" | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z"
        letramayuscula: "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I" | "J" | "K" | "L" | "M"
                    | "N" | "O" | "P" | "Q" | "R" | "S" | "T" | "U" | "V" | "W" | "X" | "Y" | "Z"
        numero: "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"

        %import common.WS
        %ignore WS
    """