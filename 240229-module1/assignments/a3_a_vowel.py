def jumlah_huruf_vokal(kata):
    i = 0
    for huruf in kata:
        if huruf.lower() in 'aiueo':
            i += 1
    return len(kata), i

print(jumlah_huruf_vokal('Surakarta'))
print(jumlah_huruf_vokal('FARHAN'))