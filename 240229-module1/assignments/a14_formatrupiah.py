def format_rupiah(nominal):
    if type(nominal) not in [int, float]:
        return "Harus bilangan bulat atau float!"
    elif nominal < 0:
        return "bilangan bulat harus positif!"
    formatted_nominal = "{:,.0f}".format(nominal)
    return f'Rp {formatted_nominal}'

print(format_rupiah(1500))
print(format_rupiah(2560000))
print("\nProgram Completed!\n\n--- By L200220277 ---")