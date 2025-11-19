def calculate_charge(pages):
    if (pages <= 100):
        charge = 0.03*pages
    elif (pages <= 300):
        charge = (0.03*100) + (pages-100) * 0.02
    else:
        charge = (0.03 * 100) + (0.02 * 200) + (pages - 300) * 0.01
    return charge

def calculate_gst(charge):
    return 0.09 * charge

print('{:5}{:>15}{:>20}'.format('Pages', 'Charge($)', 'Include GST ($)'))

for pages in range(0, 501, 50):
    charge = calculate_charge
    gst = calculate_gst(charge)
    total = charge + gst
    print('{:<5d}{:>15.2f}{:>20.2f}'.format(pages, charge, total))