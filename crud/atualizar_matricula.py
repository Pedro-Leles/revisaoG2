cursor.execute("""
    UPDATE Matriculas 
    SET status = %s 
    WHERE id_matricula = %s
""", ("Aprovado", id_matricula))
