cursor.execute("""
    SELECT nome FROM Alunos 
    WHERE TIMESTAMPDIFF(YEAR, data_nascimento, CURDATE()) >= 18
""")
