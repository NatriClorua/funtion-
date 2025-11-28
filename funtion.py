#1. kiem tra mang tang dan
def ktra_tang(arr):
    for i in range(1, len(arr)):
        if arr[i] <= arr[i-1]:
            return False
        return True

#2. kiem tra mang giam dan
def ktra_giam(arr):
    for i in range(1, len(arr)):
        if arr[i] >= arr[i-1]:
            return False
        return True
    
#3. dem so phan tu
def dem_ptu(arr):
    return len(arr)

#4. xoa phan tu lap (giu lai phan tu dau tien)
def xoa_lap(arr):
    kq =  []
    for i in arr:
        if i not in kq:
            kq.append(i)
            return kq

#5. tim vi tri xuat hien cua phan tu
def tim_vtri(arr,x):
    vtri = []
    for i in range (len(arr)):
        if arr[i] == x:
            vtri.append(i)
        return vtri
        
#6. dem so lan xuat hien cua phan tu
def dem_xh(arr):
    dem = {}
    for i in arr:
        if i in dem :
            dem [i] += 1
        else:
            dem[i] = 1
            return dem

#7. tim phan tu xuat hien nhieu nhat
def tim_xh_nhieu(arr):
    dem = dem_xh(arr)
    max_xh = 0
    phan_tu= 0
    for i in dem:
        if dem[i] > max_xh:
            max_xh = dem[i]
            phan_tu=i
            return phan_tu

#8. tim phan tu xuat hien 1 lan
def tim_xh_1lan(arr):
    dem = dem_xh(arr)
    kq = []
    for i in dem:
        if dem[i] ==1:
            kq.append(i)
            return kq

#9. tim phan tu lon nhat
def tim_max(arr):
    max_ptu = arr[0]
    for i in arr:
        if i > max_ptu :
            max_ptu = i
            return max_ptu

#10. tim phan tu nho nhat
def tim_min(arr):
    min_ptu = arr[0]
    for i in arr:
        if i< min_ptu:
            min_ptu = i
            return min_ptu

#11. tinh tong cac phan tu
def tinh_tong(arr):
    tong =0
    for i in arr:
        tong+=i
        return tong
    
#12. sap xep mang tang dan
def sx_tang(arr):
    for i in range (len(arr)):
        for j in range (i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                return arr

#13. sap xep mang giam dan
def sx_giam(arr):
    for i in range (len(arr)):
        for j in range (i+1, len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                return arr

#14. dao nguoc mang
def dao_nguoc(arr):
    kq = []
    for i in range (len(arr) -1,-1,-1):
        kq.append(arr[i])
        return kq

#15. noi 2 mang
def noi_2mang(arr1, arr2):
    return arr1+arr2

#16. lay phan tu chan
def lay_ptu_chan(arr):
    kq=[]
    for i in arr:
        if i %2 ==0:
            kq.append(i)
            return kq

#17. lay phan tu le
def lay_ptu_le(arr):
    kq = []
    for i in arr:
        if i %2 !=0:
            kq.append(i)
            return kq

#18. dem so nguyen to
def ktra_nto(n):
    if n<2:
        return False
    for i in range (2, int(n**0.5 )+1):
        if n%i ==0:
            return False
        return True
def dem_so_nto(arr):
    dem =0
    for i in arr:
        if ktra_nto(i):
            dem  +=1
            return dem

#19. tao mang rong
def tao_mang_rong():
    return []

#20. tao mang tu cac phan tu nhap vao
def tao_mang_nhap(n, ptu):
    arr = []
    for i in range (n):
        arr.append(ptu[i])
        return arr
    
#21. chen phan tu vao mang o vi tri bat ki
def chen_ptu(arr,x,vtri):
    arr.insert(vtri,x)
    return arr

#22. xoa phan tu o vi tri bat ki
def xoa_ptu(arr,vtri):
    arr.pop(vtri)
    return arr

#23. lay n phan tu dau tien
def lay_n_ptu_dau(arr,n):
    return arr[:n]

#24. lay n phan tu cuoi cung
def lay_n_ptu_cuoi(arr,n):
    return arr[-n:]

#25. tim phan tu lon thu 2
def tim_lon_thu2(arr):
    a_arr = xoa_lap(arr)
    if len(a_arr) <2:
        return None
    sx_tang(a_arr)
    return a_arr[-2]

#26. tim phan tu nho thu 2
def tim_nho_thu2(arr):
    a_arr = xoa_lap(arr)
    if len(a_arr) <2:
        return None
    sx_tang(a_arr)
    return a_arr[1]

#27. kiem tra mang doi xung
def ktra_doi_xung(arr):
    n = len(arr)
    for i in range (n//2):
        if arr[i] != arr[n -1 -i]:
            return False
        return True
    
#28. tinh tong cac phan tu chan
def tong_ptu_chan(arr):
    tong =0
    for i in arr:
        if i %2 ==0:
            tong +=i
            return tong

#29. tinh tong cac phan tu le
def tong_ptu_le(arr):
    tong =0
    for i in arr:
        if i %2 !=0:
            tong +=i
            return tong
        
#30. tim uoc so chung lon nhat cua 2 mang
def uscln_2mang(arr1, arr2):
    min_len = min(len(arr1), len(arr2) )
    uoc_so_chung =[]
    for i in range (min_len) :
        if arr1[i] == arr2[i] :
            uoc_so_chung.append(arr1[i])
        else:
            break
        return uoc_so_chung
    
#31. tim vi tri phan tu lon nhat
def tim_vtri_max(arr):
    max_ptu = tim_max(arr)
    vtri = []
    for i in range (len(arr)):
        if arr[i] == max_ptu:
            vtri.append(i)
            return vtri

#32. tim vi tri phan tu nho nhat
def tim_vtri_min(arr):
    min_ptu = tim_min(arr)
    vtri = []
    for i in range (len(arr)):
        if arr[i] == min_ptu:
            vtri.append(i)
            return vtri

#33. kiem tra mang toan duong
def ktra_toan_duong(arr):
    for i in arr:
        if i <0:
            return False
        return True

#34. kiem tra mang toan am
def ktra_toan_am(arr):
    for i in arr:
        if i >=0:
            return False
        return True

#35. chen phan tu vao vi tri dau mang
def chen_dau_mang(arr,x):
    arr.insert(0,x)
    return arr

#36. chen phan tu vao vi tri cuoi mang
def chen_cuoi_mang(arr,x):
    arr.append(x)
    return arr

#37. chen phan tu vao vi tri bat ki 
def chen_vtri_batki(arr,x,vtri):
    arr.insert(vtri,x)
    return arr

#38. xoa phan tu theo gia tri
def xoa_theo_gtri(arr,x):
    while x in arr:
        arr.remove(x)
    return arr

#39. tinh tich cac phan tu
def tinh_tich(arr):
    tich =1
    for i in arr:
        tich *=i
        return tich

#40. tim phan tu gan gia tri x nhat
def tim_gan_x_nhat(arr,x):
    gan_nhat = arr[0]
    min_khoang_cach = abs(arr[0] - x)
    for i in arr:
        khoang_cach = abs(i - x)
        if khoang_cach < min_khoang_cach:
            min_khoang_cach = khoang_cach
            gan_nhat = i
            return gan_nhat

#41. kiem tra phan tu co trong mang  hay  khong
def ktra_ptu_co_trong_mang(arr,x):
    return x in arr

#42. tinh trung binh cong cac phan tu
def tinh_tbc(arr):
    if len(arr) ==0:
        return 0
    tong = tinh_tong(arr)
    return tong / len(arr)

#43. tim phan tu lon nhat le
def tim_max_le(arr):
    le_arr = lay_ptu_le(arr)
    if not le_arr:
        return None
    return tim_max(le_arr)

#44. tim phan tu nho nhat chan
def tim_min_chan(arr):
    chan_arr = lay_ptu_chan(arr)
    if not chan_arr:
        return None
    return tim_min(chan_arr)

#45. gop 2 mang va xoa phan tu trung lap
def gop_xoa_trunglap(arr1, arr2):
    kq = arr1 + arr2
    return xoa_lap(kq)

#46. gop 2 mang va sap xep tang dan
def gop_sx_tang(arr1, arr2):
    kq = arr1 + arr2
    return sx_tang(kq)

#47. gop 2 mang va sap xep giam dan
def gop_sx_giam(arr1, arr2):
    kq = arr1 + arr2
    return sx_giam(kq)

#48. sap xep mang theo thu tu so le truoc so chan sau
def sx_le_truoc_chan(arr):
    le_arr = lay_ptu_le(arr)
    chan_arr = lay_ptu_chan(arr)
    sx_tang(le_arr)
    sx_tang(chan_arr)
    return le_arr + chan_arr

#49. sap xep mang theo thu tu so am truoc so duong sau
def sx_am_truoc_duong(arr):
    am_arr = []
    duong_arr = []
    for i in arr:
        if i <0:
            am_arr.append(i)
        else:
            duong_arr.append(i)
    sx_tang(am_arr)
    sx_tang(duong_arr)
    return am_arr + duong_arr

#50. sap xep mang theo thu tu so duong truoc so am sau
def sx_duong_truoc_am(arr):
    am_arr = []
    duong_arr = []
    for i in arr:
        if i <0:
            am_arr.append(i)
        else:
            duong_arr.append(i)
    sx_tang(duong_arr)
    sx_tang(am_arr)
    return duong_arr + am_arr

#51. kiem tra phan tu la so hoan hao
def ktra_so_hoan_hao(n):
    if n <1:
        return False
    tong_uoc =0
    for i in range (1, n):
        if n % i ==0:
            tong_uoc +=i
    return tong_uoc == n
def dem_so_hoan_hao(arr):
    dem =0
    for i in arr:
        if ktra_so_hoan_hao(i):
            dem +=1
    return dem

#52. tim so hoan hao dau tien trong mang
def tim_so_hoan_hao_dau(arr):
    for i in arr:
        if ktra_so_hoan_hao(i):
            return i
    return None

#53. tinh tong cac phan tu o vi tri chan
def tong_ptu_vtri_chan(arr):
    tong =0
    for i in range (len(arr)):
        if i %2 ==0:
            tong +=arr[i]
    return tong

#54. tinh tong cac phan tu o vi tri le
def tong_ptu_vtri_le(arr):
    tong =0
    for i in range (len(arr)):
        if i %2 !=0:
            tong +=arr[i]
    return tong

#55. sap xep mang theo thu tu tang dan o vi tri chan, giam dan o vi tri le
def sx_tang_chan_giam_le(arr):
    chan_arr = []
    le_arr = []
    for i in range (len(arr)):
        if i %2 ==0:
            chan_arr.append(arr[i])
        else:
            le_arr.append(arr[i])
    sx_tang(chan_arr)
    sx_giam(le_arr)
    kq = []
    chan_index =0
    le_index =0
    for i in range (len(arr)):
        if i %2 ==0:
            kq.append(chan_arr[chan_index])
            chan_index +=1
        else:
            kq.append(le_arr[le_index])
            le_index +=1
    return kq

#56. in ra cac phan tu 
def in_ra_ptu(arr):
    for i in arr:
        print(i)
    return None

#57. dao nguoc phan tu o vi tri chan
def dao_nguoc_vtri_chan(arr):
    chan_arr = []
    for i in range (len(arr)):
        if i %2 ==0:
            chan_arr.append(arr[i])
    chan_arr.reverse()
    kq = []
    chan_index =0
    for i in range (len(arr)):
        if i %2 ==0:
            kq.append(chan_arr[chan_index])
            chan_index +=1
        else:
            kq.append(arr[i])
    return kq

#58. dao nguoc phan tu o vi tri le
def dao_nguoc_vtri_le(arr):
    le_arr = []
    for i in range (len(arr)):
        if i %2 !=0:
            le_arr.append(arr[i])
    le_arr.reverse()
    kq = []
    le_index =0
    for i in range (len(arr)):
        if i %2 !=0:
            kq.append(le_arr[le_index])
            le_index +=1
        else:
            kq.append(arr[i])
    return kq

#59. lay n phan tu o vi tri chan
def lay_n_ptu_vtri_chan(arr,n):
    kq = []
    for i in range (len(arr)):
        if i %2 ==0:
            kq.append(arr[i])
            if len(kq) == n:
                break
    return kq

#60. lay n phan tu o vi tri le
def lay_n_ptu_vtri_le(arr,n):
    kq = []
    for i in range (len(arr)):
        if i %2 !=0:
            kq.append(arr[i])
            if len(kq) == n:
                break
    return kq

#61. hieu cua 2 mang
def hieu_2mang(arr1, arr2):
    kq = []
    for i in arr1:
        if i not in arr2:
            kq.append(i)
    return kq

#62. giao cua 2 mang
def giao_2mang(arr1, arr2):
    kq = []
    for i in arr1:
        if i in arr2:
            kq.append(i)
    return kq

#63. phan biet cac phan tu chan va le
def phan_biet_chan_le(arr):
    chan_arr = []
    le_arr = []
    for i in arr:
        if i %2 ==0:
            chan_arr.append(i)
        else:
            le_arr.append(i)
    return chan_arr, le_arr

#64. tinh trung binh cong phan tu chan
def tbc_ptu_chan(arr):
    chan_arr = lay_ptu_chan(arr)
    if not chan_arr:
        return 0
    tong = tinh_tong(chan_arr)
    return tong / len(chan_arr)

#65. tinh trung binh cong phan tu le
def tbc_ptu_le(arr):
    le_arr = lay_ptu_le(arr)
    if not le_arr:
        return 0
    tong = tinh_tong(le_arr)
    return tong / len(le_arr)

#66. tim so lon thu hai trong mang
def tim_so_lon_thu_hai(arr):
    a_arr = xoa_lap(arr)
    if len(a_arr) <2:
        return None
    sx_tang(a_arr)
    return a_arr[-2]

#67. tim so nho thu hai trong mang
def tim_so_nho_thu_hai(arr):
    a_arr = xoa_lap(arr)
    if len(a_arr) <2:
        return None
    sx_tang(a_arr)
    return a_arr[1]

#68. tinh tong tu 1 den n
def tong_1_den_n(n):
    tong =0
    for i in range (1, n+1):
        tong +=i
    return tong

#69. tinh giai thua cua n
def giai_thua(n):
    if n <0:
        return None
    tich =1
    for i in range (1, n+1):
        tich *=i
    return tich

#70. tinh tong tu m den n
def tong_m_den_n(m,n):
    if m > n:
        return 0
    tong =0
    for i in range (m, n+1):
        tong +=i
    return tong 

#71. tinh tich tu m den n
def tich_m_den_n(m,n):
    if m > n:
        return 0
    tich =1
    for i in range (m, n+1):
        tich *=i
    return tich

#72. tim vi tri phan tu lon nhat le
def tim_vtri_max_le(arr):
    le_arr = lay_ptu_le(arr)
    if not le_arr:
        return []
    max_le = tim_max(le_arr)
    vtri = []
    for i in range (len(arr)):
        if arr[i] == max_le:
            vtri.append(i)
    return vtri

#73. tim vi tri phan tu nho nhat chan
def tim_vtri_min_chan(arr):
    chan_arr = lay_ptu_chan(arr)
    if not chan_arr:
        return []
    min_chan = tim_min(chan_arr)
    vtri = []
    for i in range (len(arr)):
        if arr[i] == min_chan:
            vtri.append(i)
    return vtri

#73. tim kiem nhi phan
def tim_kiem_nhi_phan(arr, x):
    left =0
    right = len(arr) -1
    while left <= right:
        mid = (left + right) //2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid +1
        else:
            right = mid -1
    return -1

#74. tim kiem tuyen tinh
def tim_kiem_tuyen_tinh(arr,x):
    for i in range (len(arr)):
        if arr[i] == x:
            return i
    return -1

#75. tim phan tu lon hon n
def tim_ptu_lon_hon_n(arr,n):
    kq = []
    for i in arr:
        if i > n:
            kq.append(i)
        return kq

#76. tim phan tu nho hon n
def tim_ptu_nho_hon_n(arr,n):
    kq = []
    for i in arr:
        if i < n:
            kq.append(i)
        return kq

#77. tim doi xung cua mang
def tim_doi_xung_cua_mang(arr):
    kq = []
    n = len(arr)
    for i in range (n-1, -1, -1):
        kq.append(arr[i])
    return kq

#78. hop cua 2 mang 
def hop_2mang(arr1, arr2):
    kq = arr1.copy()
    for i in arr2:
        if i not in kq:
            kq.append(i)
    return kq

#79. cac phan tu xuat hien trong ca 2 mang
def ptu_xh_ca2mang(arr1, arr2):
    kq = []
    for i in arr1:
        if i in arr2 and i not in kq:
            kq.append(i)       
    return kq

#80. cac phan tu chi xuat hien trong mang thu nhat
def ptu_chi_xh_mang1(arr1, arr2):
    kq = []
    for i in arr1:
        if i not in arr2:
            kq.append(i)
    return kq

#81. cac phan tu chi xuat hien trong mang thu hai
def ptu_chi_xh_mang2(arr1, arr2):
    kq = []
    for i in arr2:
        if i not in arr1:
            kq.append(i)
    return kq

#82. cac phan tu khong trung lap cua 2 mang
def ptu_khong_trung_lap_2mang(arr1, arr2):
    kq = []
    for i in arr1:
        if i not in arr2:
            kq.append(i)
    for j in arr2:
        if j not in arr1:
            kq.append(j)
    return kq

#83. tim phan tu xuat hien it nhat
def tim_ptu_xh_it_nhat(arr):
    dem = dem_xh(arr)
    min_xh = float('inf')
    ptu_it_nhat = None
    for i in dem:
        if dem[i] < min_xh:
            min_xh = dem[i]
            ptu_it_nhat = i
    return ptu_it_nhat

#84. kiem tra mang toan so nguyen to
def ktra_toan_so_nguyen_to(arr):
    for i in arr:
        if not ktra_nto(i):
            return False
    return True 

#85. tim so nguyen to lon nhat trong mang
def tim_so_nguyen_to_lon_nhat(arr):
    nto_arr = []
    for i in arr:
        if ktra_nto(i):
            nto_arr.append(i)
    if not nto_arr:
        return None
    return tim_max(nto_arr)

#86. chen so nguyen to vao mang
def chen_so_nguyen_to(arr):
    kq = arr.copy()
    for i in range (2, 100):
        if ktra_nto(i) and i not in kq:
            kq.append(i)
    return kq

#87. xoa so nguyen to trong mang
def xoa_so_nguyen_to(arr):
    kq = []
    for i in arr:
        if not ktra_nto(i):
            kq.append(i)
    return kq

#88. tim 3 so co tong lon nhat
def tim_3so_tong_lon_nhat(arr):
    if len(arr) <3:
        return None
    sx_giam(arr)
    return arr[0], arr[1], arr[2]

#89. tim 3 so co tong nho nhat
def tim_3so_tong_nho_nhat(arr):
    if len(arr) <3:
        return None
    sx_tang(arr)
    return arr[0], arr[1], arr[2]

#90. kiem tra phan tu lap lai nhieu hon k lan
def ktra_ptu_lap_nhieu_hon_k(arr,k):
    dem = dem_xh(arr)
    for i in dem:
        if dem[i] > k:
            return True
    return False

#91. tim phan tu lap lai nhieu hon k lan
def tim_ptu_lap_nhieu_hon_k(arr,k):
    dem = dem_xh(arr)
    kq = []
    for i in dem:
        if dem[i] > k:
            kq.append(i)
    return kq

#92. dem so phan tu chan va le
def dem_so_ptu_chan_le(arr):
    dem_chan =0
    dem_le =0
    for i in arr:
        if i %2 ==0:
            dem_chan +=1
        else:
            dem_le +=1
    return dem_chan, dem_le

#93. tinh tong phan tu o vi tri chan
def tong_ptu_vtri_chan(arr):
    tong =0
    for i in range (len(arr)):
        if i %2 ==0:
            tong +=arr[i]
    return tong

#94. tinh tong phan tu o vi tri le
def tong_ptu_vtri_le(arr):
    tong =0
    for i in range (len(arr)):
        if i %2 !=0:
            tong +=arr[i]
    return tong

#95. tinh tich phan tu o vi tri chan
def tich_ptu_vtri_chan(arr):
    tich =1
    for i in range (len(arr)):
        if i %2 ==0:
            tich *=arr[i]
    return tich

#96. tinh tich phan tu o vi tri le
def tich_ptu_vtri_le(arr):
    tich =1
    for i in range (len(arr)):
        if i %2 !=0:
            tich *=arr[i]
    return tich

#97. kiem tra ma tran vuong
def ktra_ma_tran_vuong(ma_tran):
    hang = len(ma_tran)
    for row in ma_tran:
        if len(row) != hang:
            return False
    return True

#98. kiem tra ma tran chan
def ktra_ma_tran_chan(ma_tran):
    for row in ma_tran:
        for val in row:
            if val %2 !=0:
                return False
    return True

#99. kiem tra ma tran le
def ktra_ma_tran_le(ma_tran):
    for row in ma_tran:
        for val in row:
            if val %2 ==0:
                return False
    return True

#100. tao ma tran rong
def tao_ma_tran_rong(hang, cot):
    return [[0 for _ in range(cot)] for _ in range(hang)]

#101. nhap ma tran
def nhap_ma_tran(hang, cot, gia_tri):
    ma_tran = []
    index =0
    for i in range (hang):
        row = []
        for j in range (cot):
            row.append(gia_tri[index])
            index +=1
        ma_tran.append(row)
    return ma_tran

#102. in ma tran
def in_ma_tran(ma_tran):
    for row in ma_tran:
        print(' '.join(map(str, row)))
    return None

#103. tinh tong ma tran
def tinh_tong_ma_tran(ma_tran):
    tong =0
    for row in ma_tran:
        for val in row:
            tong +=val
    return tong

#104. tinh tich ma tran
def tinh_tich_ma_tran(ma_tran):
    tich =1
    for row in ma_tran:
        for val in row:
            tich *=val
    return tich

#105. tim phan tu lon nhat trong ma tran
def tim_max_ma_tran(ma_tran):
    max_ptu = ma_tran[0][0]
    for row in ma_tran:
        for val in row:
            if val > max_ptu:
                max_ptu = val
    return max_ptu

#106. tim phan tu nho nhat trong ma tran
def tim_min_ma_tran(ma_tran):
    min_ptu = ma_tran[0][0]
    for row in ma_tran:
        for val in row:
            if val < min_ptu:
                min_ptu = val
    return min_ptu

#107. lay so hang cua ma tran
def lay_so_hang(ma_tran):
    return len(ma_tran)

#108. lay so cot cua ma tran
def lay_so_cot(ma_tran):
    if not ma_tran:
        return 0
    return len(ma_tran[0])

#109. tinh tong tung hang cua ma tran
def tinh_tong_tung_hang(ma_tran):
    tong_hang = []
    for row in ma_tran:
        tong_hang.append(sum(row))
    return tong_hang

#110. tinh tong tung cot cua ma tran
def tinh_tong_tung_cot(ma_tran):
    if not ma_tran:
        return []
    so_cot = len(ma_tran[0])
    tong_cot = [0] * so_cot
    for row in ma_tran:
        for j in range(so_cot):
            tong_cot[j] += row[j]
    return tong_cot

#111. lay pha tu tai vi tri (i,j)
def lay_ptu_vi_tri(ma_tran,i,j):
    if i <0 or i >= len(ma_tran) or j <0 or j >= len(ma_tran[0]):
        return None
    return ma_tran[i][j]

#112. chen phan tu vao vi tri (i,j)
def chen_ptu_vi_tri(ma_tran,x,i,j):
    if i <0 or i >= len(ma_tran) or j <0 or j >= len(ma_tran[0]):
        return ma_tran
    ma_tran[i][j] = x
    return ma_tran

#113. xoa phan tu o vi tri (i,j)
def xoa_ptu_vi_tri(ma_tran,i,j):
    if i <0 or i >= len(ma_tran) or j <0 or j >= len(ma_tran[0]):
        return ma_tran
    ma_tran[i][j] = 0
    return ma_tran

#114. lay hang i cua ma tran
def lay_hang_i(ma_tran,i):
    if i <0 or i >= len(ma_tran):
        return None
    return ma_tran[i]

#115. lay cot j cua ma tran
def lay_cot_j(ma_tran,j):
    if not ma_tran or j <0 or j >= len(ma_tran[0]):
        return None
    cot = []
    for row in ma_tran:
        cot.append(row[j])
    return cot

#116. copy ma tran
def copy_ma_tran(ma_tran):
    kq = []
    for row in ma_tran:
        kq.append(row.copy())
    return kq

#117. dao nguoc ma tran
def dao_nguoc_ma_tran(ma_tran):
    kq = []
    for i in range (len(ma_tran)-1, -1, -1):
        kq.append(ma_tran[i])
    return kq

#118. cong 2 ma tran
def cong_2_ma_tran(ma_tran1, ma_tran2):
    if len(ma_tran1) != len(ma_tran2) or len(ma_tran1[0]) != len(ma_tran2[0]):
        return None
    kq = []
    for i in range (len(ma_tran1)):
        row = []
        for j in range (len(ma_tran1[0])):
            row.append(ma_tran1[i][j] + ma_tran2[i][j])
        kq.append(row)
    return kq

#119. nhan 2 ma tran
def nhan_2_ma_tran(ma_tran1, ma_tran2):
    if len(ma_tran1[0]) != len(ma_tran2):
        return None
    kq = []
    for i in range (len(ma_tran1)):
        row = []
        for j in range (len(ma_tran2[0])):
            sum_product =0
            for k in range (len(ma_tran1[0])):
                sum_product += ma_tran1[i][k] * ma_tran2[k][j]
            row.append(sum_product)
        kq.append(row)
    return kq

#120. tru 2 ma tran
def tru_2_ma_tran(ma_tran1, ma_tran2):
    if len(ma_tran1) != len(ma_tran2) or len(ma_tran1[0]) != len(ma_tran2[0]):
        return None
    kq = []
    for i in range (len(ma_tran1)):
        row = []
        for j in range (len(ma_tran1[0])):
            row.append(ma_tran1[i][j] - ma_tran2[i][j])
        kq.append(row)
    return kq

#121. nhan ma tran voi so
def nhan_ma_tran_voi_so(ma_tran, x):
    kq = []
    for row in ma_tran:
        new_row = []
        for val in row:
            new_row.append(val * x)
        kq.append(new_row)
    return kq

#122. tinh tong tat ca cac phan tu
def tinh_tong_tat_ca_ptu(ma_tran):
    tong =0
    for row in ma_tran:
        for val in row:
            tong +=val
    return tong

#123. tinh tich tat ca cac phan tu
def tinh_tich_tat_ca_ptu(ma_tran):
    tich =1
    for row in ma_tran:
        for val in row:
            tich *=val
    return tich

#124. tim phan tu lon nhat
def tim_ptu_lon_nhat_ma_tran(ma_tran):
    max_ptu = ma_tran[0][0]
    for row in ma_tran:
        for val in row:
            if val > max_ptu:
                max_ptu = val
    return max_ptu

#125. tim phan tu nho nhat
def tim_ptu_nho_nhat_ma_tran(ma_tran):
    min_ptu = ma_tran[0][0]
    for row in ma_tran:
        for val in row:
            if val < min_ptu:
                min_ptu = val
    return min_ptu

#126. tinh tong tung hang
def tinh_tong_tung_hang_ma_tran(ma_tran):
    tong_hang = []
    for row in ma_tran:
        tong_hang.append(sum(row))
    return tong_hang

#127. tinh tong tung cot
def tinh_tong_tung_cot_ma_tran(ma_tran):
    if not ma_tran:
        return []
    so_cot = len(ma_tran[0])
    tong_cot = [0] * so_cot
    for row in ma_tran:
        for j in range(so_cot):
            tong_cot[j] += row[j]
    return tong_cot

#128. chuyen vi ma tran
def chuyen_vi_ma_tran(ma_tran):
    if not ma_tran:
        return []
    so_hang = len(ma_tran)
    so_cot = len(ma_tran[0])
    kq = []
    for j in range (so_cot):
        new_row = []
        for i in range (so_hang):
            new_row.append(ma_tran[i][j])
        kq.append(new_row)
    return kq

#129. kiem tra ma tran vuong
def ktra_ma_tran_vuong(ma_tran):
    if not ma_tran:
        return False
    so_hang = len(ma_tran)
    for row in ma_tran:
        if len(row) != so_hang:
            return False
    return True

#130. dao nguoc tung hang
def dao_nguoc_tung_hang(ma_tran):
    kq = []
    for row in ma_tran:
        kq.append(row[::-1])
    return kq

#131. dao nguoc tung cot
def dao_nguoc_tung_cot(ma_tran):
    if not ma_tran:
        return []
    so_hang = len(ma_tran)
    so_cot = len(ma_tran[0])
    kq = []
    for j in range (so_cot):
        new_row = []
        for i in range (so_hang-1, -1, -1):
            new_row.append(ma_tran[i][j])
        kq.append(new_row)
    return kq

#132. tinh tong duong cheo chinh
def tinh_tong_duong_cheo_chinh(ma_tran):
    if not ktra_ma_tran_vuong(ma_tran):
        return None
    tong =0
    for i in range (len(ma_tran)):
        tong += ma_tran[i][i]
    return tong

#133. tim hang co tong lon nhat
def tim_hang_co_tong_lon_nhat(ma_tran):
    max_tong = float('-inf')
    hang_index = -1
    for i in range (len(ma_tran)):
        tong_hang = sum(ma_tran[i])
        if tong_hang > max_tong:
            max_tong = tong_hang
            hang_index = i
    return hang_index

#134. tim cot co tong nho nhat
def tim_cot_co_tong_nho_nhat(ma_tran):
    if not ma_tran:
        return -1
    so_cot = len(ma_tran[0])
    min_tong = float('inf')
    cot_index = -1
    for j in range (so_cot):
        tong_cot =0
        for i in range (len(ma_tran)):
            tong_cot += ma_tran[i][j]
        if tong_cot < min_tong:
            min_tong = tong_cot
            cot_index = j
    return cot_index

#135. hoán đổi 2 hang trong ma tran
def hoan_doi_2_hang(ma_tran, hang1, hang2):
    if hang1 <0 or hang1 >= len(ma_tran) or hang2 <0 or hang2 >= len(ma_tran):
        return ma_tran
    ma_tran[hang1], ma_tran[hang2] = ma_tran[hang2], ma_tran[hang1]
    return ma_tran

#136. hoán đổi 2 cot trong ma tran
def hoan_doi_2_cot(ma_tran, cot1, cot2):
    if not ma_tran:
        return ma_tran
    so_cot = len(ma_tran[0])
    if cot1 <0 or cot1 >= so_cot or cot2 <0 or cot2 >= so_cot:
        return ma_tran
    for row in ma_tran:
        row[cot1], row[cot2] = row[cot2], row[cot1]
    return ma_tran

#137. tinh trung binh cong ma tran
def tinh_tbc_ma_tran(ma_tran):
    tong =0
    dem =0
    for row in ma_tran:
        for val in row:
            tong +=val
            dem +=1
    if dem ==0:
        return 0
    return tong / dem

#138. tinh trung binh cong tung hang
def tinh_tbc_tung_hang(ma_tran):
    tbc_hang = []
    for row in ma_tran:
        if len(row) ==0:
            tbc_hang.append(0)
        else:
            tbc_hang.append(sum(row) / len(row))
    return tbc_hang

#139. tinh trung binh cong tung cot
def tinh_tbc_tung_cot(ma_tran):
    if not ma_tran:
        return []
    so_cot = len(ma_tran[0])
    tbc_cot = []
    for j in range (so_cot):
        tong_cot =0
        dem =0
        for i in range (len(ma_tran)):
            tong_cot += ma_tran[i][j]
            dem +=1
        if dem ==0:
            tbc_cot.append(0)
        else:
            tbc_cot.append(tong_cot / dem)
    return tbc_cot

#140. tim so nguyen to trong ma tran
def tim_so_nguyen_to_trong_ma_tran(ma_tran):
    nto_arr = []
    for row in ma_tran:
        for val in row:
            if ktra_nto(val):
                nto_arr.append(val)
    return nto_arr

#141. tim so lon nhat trong ma tran
def tim_so_lon_nhat_trong_ma_tran(ma_tran):
    max_ptu = ma_tran[0][0]
    for row in ma_tran:
        for val in row:
            if val > max_ptu:
                max_ptu = val
    return max_ptu

#142. tim so nho nhat trong ma tran
def tim_so_nho_nhat_trong_ma_tran(ma_tran):
    min_ptu = ma_tran[0][0]
    for row in ma_tran:
        for val in row:
            if val < min_ptu:
                min_ptu = val
    return min_ptu

#143. dem so nguyen to trong ma tran
def dem_so_nguyen_to_trong_ma_tran(ma_tran):
    dem =0
    for row in ma_tran:
        for val in row:
            if ktra_nto(val):
                dem +=1
    return dem

#144. tinh tong so nguyen to trong ma tran
def tong_so_nguyen_to_trong_ma_tran(ma_tran):
    tong =0
    for row in ma_tran:
        for val in row:
            if ktra_nto(val):
                tong +=val
    return tong

#145. tim phan tu lon thu 2 trong ma tran
def tim_ptu_lon_thu2_ma_tran(ma_tran):
    flat_arr = []
    for row in ma_tran:
        flat_arr.extend(row)
    a_arr = xoa_lap(flat_arr)
    if len(a_arr) <2:
        return None
    sx_tang(a_arr)
    return a_arr[-2]

#146. tim phan tu nho thu 2 trong ma tran
def tim_ptu_nho_thu2_ma_tran(ma_tran):
    flat_arr = []
    for row in ma_tran:
        flat_arr.extend(row)
    a_arr = xoa_lap(flat_arr)
    if len(a_arr) <2:
        return None
    sx_tang(a_arr)
    return a_arr[1]

#147. tim phan tu trong ma tran 
def tim_ptu_trong_ma_tran(ma_tran,x):
    for i in range (len(ma_tran)):
        for j in range (len(ma_tran[0])):
            if ma_tran[i][j] == x:
                return (i,j)
    return None

#148. tim phan tu chan lon nhat trong ma tran
def tim_ptu_chan_lon_nhat_ma_tran(ma_tran):
    chan_arr = []
    for row in ma_tran:
        for val in row:
            if val %2 ==0:
                chan_arr.append(val)
    if not chan_arr:
        return None
    return tim_max(chan_arr)

#149. tim phan tu le nho nhat trong ma tran
def tim_ptu_le_nho_nhat_ma_tran(ma_tran):
    le_arr = []
    for row in ma_tran:
        for val in row:
            if val %2 !=0:
                le_arr.append(val)
    if not le_arr:
        return None
    return tim_min(le_arr)

#150. kiem tra phan tu co trong ma tran
def ktra_ptu_co_trong_ma_tran(ma_tran,x):
    for row in ma_tran:
        if x in row:
            return True
    return False

#151. dem so lan xuat hien cua phan tu trong ma tran
def dem_so_lan_xh_ptu_trong_ma_tran(ma_tran,x):
    dem =0
    for row in ma_tran:
        for val in row:
            if val == x:
                dem +=1
    return dem

#152. tim hang chua phan tu lon nhat
def tim_hang_chua_ptu_lon_nhat(ma_tran):
    max_ptu = tim_so_lon_nhat_trong_ma_tran(ma_tran)
    for i in range (len(ma_tran)):
        if max_ptu in ma_tran[i]:
            return i
    return -1

#153. tim cot chua phan tu nho nhat
def tim_cot_chua_ptu_nho_nhat(ma_tran):
    min_ptu = tim_so_nho_nhat_trong_ma_tran(ma_tran)
    so_cot = len(ma_tran[0])
    for j in range (so_cot):
        for i in range (len(ma_tran)):
            if ma_tran[i][j] == min_ptu:
                return j
    return -1

#154. tim hang chua phan tu
def tim_hang_chua_ptu(ma_tran,x):
    for i in range (len(ma_tran)):
        if x in ma_tran[i]:
            return i
    return -1

#155. tim cot chua phan tu
def tim_cot_chua_ptu(ma_tran,x):
    so_cot = len(ma_tran[0])
    for j in range (so_cot):
        for i in range (len(ma_tran)):
            if ma_tran[i][j] == x:
                return j
    return -1

#156. tinh tong phan tu o vi tri chan
def tong_ptu_o_vtri_chan_ma_tran(ma_tran):
    tong =0
    for i in range (len(ma_tran)):
        for j in range (len(ma_tran[0])):
            if (i + j) %2 ==0:
                tong += ma_tran[i][j]
    return tong 

#157. tinh tong phan tu o vi tri le
def tong_ptu_o_vtri_le_ma_tran(ma_tran):
    tong =0
    for i in range (len(ma_tran)):
        for j in range (len(ma_tran[0])):
            if (i + j) %2 !=0:
                tong += ma_tran[i][j]
    return tong

#158. sap xep tung hang cua ma tran theo thu tu tang dan
def sx_tung_hang_tang_dan_ma_tran(ma_tran):
    kq = []
    for row in ma_tran:
        sx_tang(row)
        kq.append(row)
    return kq

#159. sap xep tung hang cua ma tran theo thu tu giam dan
def sx_tung_hang_giam_dan_ma_tran(ma_tran):
    kq = []
    for row in ma_tran:
        sx_giam(row)
        kq.append(row)
    return kq

#160. sap xep tung cot cua ma tran theo thu tu tang dan
def sx_tung_cot_tang_dan_ma_tran(ma_tran):
    if not ma_tran:
        return []
    so_cot = len(ma_tran[0])
    kq = copy_ma_tran(ma_tran)
    for j in range (so_cot):
        cot = []
        for i in range (len(kq)):
            cot.append(kq[i][j])
        sx_tang(cot)
        for i in range (len(kq)):
            kq[i][j] = cot[i]
    return kq

#161. sap xep tung cot cua ma tran theo thu tu giam dan
def sx_tung_cot_giam_dan_ma_tran(ma_tran):
    if not ma_tran:
        return []
    so_cot = len(ma_tran[0])
    kq = copy_ma_tran(ma_tran)
    for j in range (so_cot):
        cot = []
        for i in range (len(kq)):
            cot.append(kq[i][j])
        sx_giam(cot)
        for i in range (len(kq)):
            kq[i][j] = cot[i]
    return kq

#162. tim kiem vi tri phan tu x trong ma tran
def tim_kiem_vi_tri_ptu_x_trong_ma_tran(ma_tran,x):
    vtri = []
    for i in range (len(ma_tran)):
        for j in range (len(ma_tran[0])):
            if ma_tran[i][j] == x:
                vtri.append((i,j))
    return vtri

#162. dem so phan tu lon hon x trong ma tran
def dem_so_ptu_lon_hon_x_trong_ma_tran(ma_tran,x):
    dem =0
    for row in ma_tran:
        for val in row:
            if val > x:
                dem +=1
    return dem

#164. dem so phan tu nho hon x trong ma tran
def dem_so_ptu_nho_hon_x_trong_ma_tran(ma_tran,x):
    dem =0
    for row in ma_tran:
        for val in row:
            if val < x:
                dem +=1
    return dem

#165. sap xep ma tran theo thu tu tang dan
def sx_ma_tran_tang_dan(ma_tran):
    flat_arr = []
    for row in ma_tran:
        flat_arr.extend(row)
    sx_tang(flat_arr)
    kq = []
    index =0
    for i in range (len(ma_tran)):
        new_row = []
        for j in range (len(ma_tran[0])):
            new_row.append(flat_arr[index])
            index +=1
        kq.append(new_row)
    return kq

#166. sap xep ma tran theo thu tu giam dan
def sx_ma_tran_giam_dan(ma_tran):
    flat_arr = []
    for row in ma_tran:
        flat_arr.extend(row)
    sx_giam(flat_arr)
    kq = []
    index =0
    for i in range (len(ma_tran)):
        new_row = []
        for j in range (len(ma_tran[0])):
            new_row.append(flat_arr[index])
            index +=1
        kq.append(new_row)
    return kq

#167. dem so phan tu chan trong ma tran
def dem_so_ptu_chan_trong_ma_tran(ma_tran):
    dem =0
    for row in ma_tran:
        for val in row:
            if val %2 ==0:
                dem +=1
    return dem

#168. dem so phan tu le trong ma tran
def dem_so_ptu_le_trong_ma_tran(ma_tran):
    dem =0
    for row in ma_tran:
        for val in row:
            if val %2 !=0:
                dem +=1
    return dem

#169. dao nguoc tung cot trong ma tran
def dao_nguoc_tung_cot_ma_tran(ma_tran):
    if not ma_tran:
        return []
    so_hang = len(ma_tran)
    so_cot = len(ma_tran[0])
    kq = copy_ma_tran(ma_tran)
    for j in range (so_cot):
        top =0
        bottom = so_hang -1
        while top < bottom:
            kq[top][j], kq[bottom][j] = kq[bottom][j], kq[top][j]
            top +=1
            bottom -=1
    return kq

#170. dao nguoc tung hang trong ma tran
def dao_nguoc_tung_hang_ma_tran(ma_tran):
    kq = []
    for i in range (len(ma_tran)-1, -1, -1):
        kq.append(ma_tran[i])
    return kq

#171. lay n phan tu chan dau tien trong ma tran
def lay_n_ptu_chan_dau_tien_ma_tran(ma_tran,n):
    kq = []
    for i in range (len(ma_tran)):
        for j in range (len(ma_tran[0])):
            if ma_tran[i][j] %2 ==0:
                kq.append(ma_tran[i][j])
                if len(kq) == n:
                    return kq
    return kq

#172. lay n phan tu le dau tien trong ma tran
def lay_n_ptu_le_dau_tien_ma_tran(ma_tran,n):
    kq = []
    for i in range (len(ma_tran)):
        for j in range (len(ma_tran[0])):
            if ma_tran[i][j] %2 !=0:
                kq.append(ma_tran[i][j])
                if len(kq) == n:
                    return kq
    return kq

#173. xoa hang i trong ma tran
def xoa_hang_i_ma_tran(ma_tran,i):
    if i <0 or i >= len(ma_tran):
        return ma_tran
    kq = []
    for j in range (len(ma_tran)):
        if j != i:
            kq.append(ma_tran[j])
    return kq

#174. xoa cot j trong ma tran
def xoa_cot_j_ma_tran(ma_tran,j):
    if not ma_tran:
        return ma_tran
    so_cot = len(ma_tran[0])
    if j <0 or j >= so_cot:
        return ma_tran
    kq = []
    for i in range (len(ma_tran)):
        new_row = []
        for col in range (so_cot):
            if col != j:
                new_row.append(ma_tran[i][col])
        kq.append(new_row)
    return kq

#175. them hang vao ma tran
def them_hang_vao_ma_tran(ma_tran,new_row):
    if len(ma_tran) >0 and len(new_row) != len(ma_tran[0]):
        return ma_tran
    kq = copy_ma_tran(ma_tran)
    kq.append(new_row)
    return kq

#176. them cot vao ma tran
def them_cot_vao_ma_tran(ma_tran,new_col):
    if not ma_tran:
        return ma_tran
    so_hang = len(ma_tran)
    if len(new_col) != so_hang:
        return ma_tran
    kq = copy_ma_tran(ma_tran)
    for i in range (so_hang):
        kq[i].append(new_col[i])
    return kq

#177. kiem tra ma tran co phai la ma tran don vi
def ktra_ma_tran_don_vi(ma_tran):
    if not ktra_ma_tran_vuong(ma_tran):
        return False
    for i in range (len(ma_tran)):
        for j in range (len(ma_tran)):
            if i == j:
                if ma_tran[i][j] !=1:
                    return False
            else:
                if ma_tran[i][j] !=0:
                    return False
    return True

#178. kiem tra ma tran co phai la ma tran doi xung
def ktra_ma_tran_doi_xung(ma_tran):
    if not ktra_ma_tran_vuong(ma_tran):
        return False
    n = len(ma_tran)
    for i in range (n):
        for j in range (i+1, n):
            if ma_tran[i][j] != ma_tran[j][i]:
                return False
    return True

#179. tim vi tri phan tu lon nhat trong ma tran
def tim_vi_tri_ptu_lon_nhat_ma_tran(ma_tran):
    max_ptu = ma_tran[0][0]
    vtri = (0,0)
    for i in range (len(ma_tran)):
        for j in range (len(ma_tran[0])):
            if ma_tran[i][j] > max_ptu:
                max_ptu = ma_tran[i][j]
                vtri = (i,j)
    return vtri

#180. tim vi tri phan tu nho nhat trong ma tran
def tim_vi_tri_ptu_nho_nhat_ma_tran(ma_tran):
    min_ptu = ma_tran[0][0]
    vtri = (0,0)
    for i in range (len(ma_tran)):
        for j in range (len(ma_tran[0])):
            if ma_tran[i][j] < min_ptu:
                min_ptu = ma_tran[i][j]
                vtri = (i,j)
    return vtri

#181. tim vi tri phan tu x trong ma tran
def tim_vi_tri_ptu_x_ma_tran(ma_tran,x):
    vtri = []
    for i in range (len(ma_tran)):
        for j in range (len(ma_tran[0])):
            if ma_tran[i][j] == x:
                vtri.append((i,j))
    return vtri

#182. tinh tong duong cheo phu cua ma tran
def tinh_tong_duong_cheo_phu_ma_tran(ma_tran):
    if not ktra_ma_tran_vuong(ma_tran):
        return None
    tong =0
    n = len(ma_tran)
    for i in range (n):
        tong += ma_tran[i][n -1 - i]
    return tong

#183. tinh tich duong cheo chinh cua ma tran
def tinh_tich_duong_cheo_chinh_ma_tran(ma_tran):
    if not ktra_ma_tran_vuong(ma_tran):
        return None
    tich =1
    for i in range (len(ma_tran)):
        tich *= ma_tran[i][i]
    return tich

#184. tinh tich duong cheo phu cua ma tran
def tinh_tich_duong_cheo_phu_ma_tran(ma_tran):
    if not ktra_ma_tran_vuong(ma_tran):
        return None
    tich =1
    n = len(ma_tran)
    for i in range (n):
        tich *= ma_tran[i][n -1 - i]
    return tich

#185. kiem tra ma tran co phai la ma tran don vi khong
def ktra_ma_tran_don_vi_khong(ma_tran):
    if not ktra_ma_tran_vuong(ma_tran):
        return False
    for i in range (len(ma_tran)):
        for j in range (len(ma_tran)):
            if i == j:
                if ma_tran[i][j] !=0:
                    return False
            else:
                if ma_tran[i][j] !=1:
                    return False
    return True

#186. tinh tong so hang va so cot cua ma tran
def tinh_tong_so_hang_va_so_cot_ma_tran(ma_tran):
    so_hang = len(ma_tran)
    if so_hang ==0:
        return 0
    so_cot = len(ma_tran[0])
    return so_hang + so_cot

#187. tinh tong cac so nguyen to tren duong cheo chinh
def tinh_tong_so_nguyen_to_tren_duong_cheo_chinh_ma_tran(ma_tran):
    if not ktra_ma_tran_vuong(ma_tran):
        return None
    tong =0
    for i in range (len(ma_tran)):
        if ktra_nto(ma_tran[i][i]):
            tong += ma_tran[i][i]
    return tong

#188. tinh tong cac so nguyen to tren duong cheo phu
def tinh_tong_so_nguyen_to_tren_duong_cheo_phu_ma_tran(ma_tran):
    if not ktra_ma_tran_vuong(ma_tran):
        return None
    tong =0
    n = len(ma_tran)
    for i in range (n):
        if ktra_nto(ma_tran[i][n -1 - i]):
            tong += ma_tran[i][n -1 - i]
    return tong

#189. tinh tich cac so nguyen to tren duong cheo chinh
def tinh_tich_so_nguyen_to_tren_duong_cheo_chinh_ma_tran(ma_tran):
    if not ktra_ma_tran_vuong(ma_tran):
        return None
    tich =1
    for i in range (len(ma_tran)):
        if ktra_nto(ma_tran[i][i]):
            tich *= ma_tran[i][i]
    return tich

#190. tinh tich cac so nguyen to tren duong cheo phu
def tinh_tich_so_nguyen_to_tren_duong_cheo_phu_ma_tran(ma_tran):
    if not ktra_ma_tran_vuong(ma_tran):
        return None
    tich =1
    n = len(ma_tran)
    for i in range (n):
        if ktra_nto(ma_tran[i][n -1 - i]):
            tich *= ma_tran[i][n -1 - i]
    return tich

#191. kiem tra ma tran co toan le khong
def ktra_ma_tran_toan_le(ma_tran):
    for row in ma_tran:
        for val in row:
            if val %2 ==0:
                return False
    return True
#192. kiem tra ma tran co toan chan khong
def ktra_ma_tran_toan_chan(ma_tran):
    for row in ma_tran:
        for val in row:
            if val %2 !=0:
                return False
    return True

#193. tao ma tran
def tao_ma_tran(hang, cot):
    ma_tran = []
    for i in range (hang):
        row = []
        for j in range (cot):
            row.append(0)
        ma_tran.append(row)
    return ma_tran

#194. in ma tran
def in_ma_tran(ma_tran):
    for row in ma_tran:
        print(row)
        
#195. tinh tong ma tran 
def tinh_tong_ma_tran(ma_tran):
    tong =0
    for row in ma_tran:
        for val in row:
            tong +=val
    return tong

#196. tinh tich ma tran
def tinh_tich_ma_tran(ma_tran):
    tich =1
    for row in ma_tran:
        for val in row:
            tich *=val
    return tich

#197. tim phan tu lon thu 2 trong ma tran
def tim_ptu_lon_thu2_trong_ma_tran(ma_tran):
    flat_arr = []
    for row in ma_tran:
        flat_arr.extend(row)
    a_arr = xoa_lap(flat_arr)
    if len(a_arr) <2:
        return None
    sx_tang(a_arr)
    return a_arr[-2]

#198. tim phan tu nho thu 2 trong ma tran
def tim_ptu_nho_thu2_trong_ma_tran(ma_tran):
    flat_arr = []
    for row in ma_tran:
        flat_arr.extend(row)
    a_arr = xoa_lap(flat_arr)
    if len(a_arr) <2:
        return None
    sx_tang(a_arr)
    return a_arr[1]

#199. dem so phan tu trong ma tran
def dem_so_ptu_trong_ma_tran(ma_tran):
    dem =0
    for row in ma_tran:
        dem += len(row)
    return dem

#200. tinh tong tung hang cua ma tran
def tinh_tong_tung_hang_ma_tran(ma_tran):
    tong_hang = []
    for row in ma_tran:
        tong_hang.append(sum(row))
    return tong_hang

#201. tinh tong tung cot cua ma tran
def tinh_tong_tung_cot_ma_tran(ma_tran):
    if not ma_tran:
        return []
    so_cot = len(ma_tran[0])
    tong_cot = [0] * so_cot
    for row in ma_tran:
        for j in range(so_cot):
            tong_cot[j] += row[j]
    return tong_cot

#202. lay phan tu o vi tri (i,j)
def lay_ptu_vi_tri(ma_tran,i,j):
    if i <0 or i >= len(ma_tran) or j <0 or j >= len(ma_tran[0]):
        return None
    return ma_tran[i][j]

#203. them phan tu x o vi tri (i,j)
def them_ptu_vi_tri(ma_tran,i,j,x):
    if i <0 or i >= len(ma_tran) or j <0 or j >= len(ma_tran[0]):
        return ma_tran
    ma_tran[i][j] = x
    return ma_tran

#204. xoa phan tu o vi tri (i,j)
def xoa_ptu_vi_tri(ma_tran,i,j):
    if i <0 or i >= len(ma_tran) or j <0 or j >= len(ma_tran[0]):
        return ma_tran
    ma_tran[i][j] =0
    return ma_tran

#205. thay the phan tu o vi tri (i,j) bang x
def thay_the_ptu_vi_tri(ma_tran,i,j,x):
    if i <0 or i >= len(ma_tran) or j <0 or j >= len(ma_tran[0]):
        return ma_tran
    ma_tran[i][j] = x
    return ma_tran