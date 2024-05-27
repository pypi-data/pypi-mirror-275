import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from scipy.spatial.distance import euclidean, cityblock, jaccard, hamming, dice
from scipy.stats import pearsonr
from scipy.special import rel_entr

# CSVファイルの読み込み
def read_csv(csv, A=None, B=None):
    vec_A = []
    vec_B = []
    data = np.loadtxt(csv, delimiter=",", skiprows=1)
    if (B is None) and (A is not None):
        vec_A.append(data[A])
        for i in range(len(data)):
            vec_B.append(data[i])
    elif (B is None) and (A is None):
        for j in range(len(data)):
            vec_A.append(data[j])
            vec_B.append(data[j])
    else:
        vec_A.append(data[A])
        vec_B.append(data[B])
    return vec_A, vec_B

# コサイン類似度の計算
def Cosine(csv, A=None, B=None):
    cos_sim_list = []
    if (B is None) and (A is not None):
        vec_A, vec_B = read_csv(csv, A-2)
        Vec_A = vec_A[0].reshape(1, -1)
        for k in range(len(vec_B)):
            if k == A-2:
                continue
            Vec_B = vec_B[k].reshape(1, -1)
            cos_sim_list.append([[A, k+2], cosine_similarity(Vec_A, Vec_B)[0][0]])

    elif (B is None) and (A is None):
        vec_A, vec_B = read_csv(csv)
        for n in range(len(vec_A)):
            for m in range(n, len(vec_B)):
                if n == m:
                    continue
                Vec_A = vec_A[n].reshape(1, -1)
                Vec_B = vec_B[m].reshape(1, -1)
                cos_sim_list.append([[n+2, m+2], cosine_similarity(Vec_A, Vec_B)[0][0]])
    else:
        vec_A, vec_B = read_csv(csv, A-2, B-2)
        Vec_A = vec_A[0].reshape(1, -1)
        Vec_B = vec_B[0].reshape(1, -1)
        cos_sim_list.append([[A, B], cosine_similarity(Vec_A, Vec_B)[0][0]])
    return_cos_sim_list = sorted(cos_sim_list, key=lambda x: x[1], reverse=True)[:10]
    return return_cos_sim_list

# ユークリッド距離の計算
def Euclidean(csv, A=None, B=None):
    euclidean_list = []
    if (B is None) and (A is not None):
        vec_A, vec_B = read_csv(csv, A-2)
        Vec_A = vec_A[0].reshape(1, -1)
        for k in range(len(vec_B)):
            if k == A-2:
                continue
            Vec_B = vec_B[k].reshape(1, -1)
            euclidean_list.append([[A, k+2], euclidean(Vec_A.flatten(), Vec_B.flatten())])
    elif (B is None) and (A is None):
        vec_A, vec_B = read_csv(csv)
        for n in range(len(vec_A)):
            for m in range(n, len(vec_B)):
                if n == m:
                    continue
                Vec_A = vec_A[n].reshape(1, -1)
                Vec_B = vec_B[m].reshape(1, -1)
                euclidean_list.append([[n+2, m+2], euclidean(Vec_A.flatten(), Vec_B.flatten())])
    else:
        vec_A, vec_B = read_csv(csv, A-2, B-2)
        Vec_A = vec_A[0].reshape(1, -1)
        Vec_B = vec_B[0].reshape(1, -1)
        euclidean_list.append([[A, B], euclidean(Vec_A.flatten(), Vec_B.flatten())])
    return_euclidean_list = sorted(euclidean_list, key=lambda x: x[1])[:10]
    return return_euclidean_list

# マンハッタン距離の計算
def Manhattan(csv, A=None, B=None):
    manhattan_list = []
    if (B is None) and (A is not None):
        vec_A, vec_B = read_csv(csv, A-2)
        Vec_A = vec_A[0].reshape(1, -1)
        for k in range(len(vec_B)):
            if k == A-2:
                continue
            Vec_B = vec_B[k].reshape(1, -1)
            manhattan_list.append([[A, k+2], cityblock(Vec_A.flatten(), Vec_B.flatten())])
    elif (B is None) and (A is None):
        vec_A, vec_B = read_csv(csv)
        for n in range(len(vec_A)):
            for m in range(n, len(vec_B)):
                if n == m:
                    continue
                Vec_A = vec_A[n].reshape(1, -1)
                Vec_B = vec_B[m].reshape(1, -1)
                manhattan_list.append([[n+2, m+2], cityblock(Vec_A.flatten(), Vec_B.flatten())])
    else:
        vec_A, vec_B = read_csv(csv, A-2, B-2)
        Vec_A = vec_A[0].reshape(1, -1)
        Vec_B = vec_B[0].reshape(1, -1)
        manhattan_list.append([[A, B], cityblock(Vec_A.flatten(), Vec_B.flatten())])
    sorted_manhattan_list = sorted(manhattan_list, key=lambda x: x[1])[:10]
    return sorted_manhattan_list

# ジャカード係数の計算
def Jaccard(csv, A=None, B=None):
    jaccard_list = []
    if (B is None) and (A is not None):
        vec_A, vec_B = read_csv(csv, A-2)
        Vec_A = vec_A[0].reshape(1, -1)
        for k in range(len(vec_B)):
            if k == A-2:
                continue
            Vec_B = vec_B[k].reshape(1, -1)
            jaccard_list.append([[A, k+2], 1 - jaccard(Vec_A.flatten(), Vec_B.flatten())])
    elif (B is None) and (A is None):
        vec_A, vec_B = read_csv(csv)
        for n in range(len(vec_A)):
            for m in range(n, len(vec_B)):
                if n == m:
                    continue
                Vec_A = vec_A[n].reshape(1, -1)
                Vec_B = vec_B[m].reshape(1, -1)
                jaccard_list.append([[n+2, m+2], 1 - jaccard(Vec_A.flatten(), Vec_B.flatten())])
    else:
        vec_A, vec_B = read_csv(csv, A-2, B-2)
        Vec_A = vec_A[0].reshape(1, -1)
        Vec_B = vec_B[0].reshape(1, -1)
        jaccard_list.append([[A, B], 1 - jaccard(Vec_A.flatten(), Vec_B.flatten())])
    sorted_jaccard_list = sorted(jaccard_list, key=lambda x: x[1], reverse=True)[:10]
    return sorted_jaccard_list

# ハミング距離の計算
def Hamming(csv, A=None, B=None):
    hamming_list = []
    if (B is None) and (A is not None):
        vec_A, vec_B = read_csv(csv, A-2)
        Vec_A = vec_A[0].reshape(1, -1)
        for k in range(len(vec_B)):
            if k == A-2:
                continue
            Vec_B = vec_B[k].reshape(1, -1)
            hamming_list.append([[A, k+2], hamming(Vec_A.flatten(), Vec_B.flatten())])
    elif (B is None) and (A is None):
        vec_A, vec_B = read_csv(csv)
        for n in range(len(vec_A)):
            for m in range(n, len(vec_B)):
                if n == m:
                    continue
                Vec_A = vec_A[n].reshape(1, -1)
                Vec_B = vec_B[m].reshape(1, -1)
                hamming_list.append([[n+2, m+2], hamming(Vec_A.flatten(), Vec_B.flatten())])
    else:
        vec_A, vec_B = read_csv(csv, A-2, B-2)
        Vec_A = vec_A[0].reshape(1, -1)
        Vec_B = vec_B[0].reshape(1, -1)
        hamming_list.append([[A, B], hamming(Vec_A.flatten(), Vec_B.flatten())])
    return_hamming_list = sorted(hamming_list, key=lambda x: x[1])[:10]
    return return_hamming_list

# ピアソン相関係数の計算
def Pearson(csv, A=None, B=None):
    pearson_list = []
    if (B is None) and (A is not None):
        vec_A, vec_B = read_csv(csv, A-2)
        Vec_A = vec_A[0].reshape(1, -1)
        for k in range(len(vec_B)):
            if k == A-2:
                continue
            Vec_B = vec_B[k].reshape(1, -1)
            result_pearson, _ = pearsonr(Vec_A.flatten(), Vec_B.flatten())
            pearson_list.append([[A, k+2], result_pearson])
    elif (B is None) and (A is None):
        vec_A, vec_B = read_csv(csv)
        for n in range(len(vec_A)):
            for m in range(n, len(vec_B)):
                if n == m:
                    continue
                Vec_A = vec_A[n].reshape(1, -1)
                Vec_B = vec_B[m].reshape(1, -1)
                result_pearson, _ = pearsonr(Vec_A.flatten(), Vec_B.flatten())
                pearson_list.append([[n+2, m+2], result_pearson])
    else:
        vec_A, vec_B = read_csv(csv, A-2, B-2)
        Vec_A = vec_A[0].reshape(1, -1)
        Vec_B = vec_B[0].reshape(1, -1)
        result_pearson, _ = pearsonr(Vec_A.flatten(), Vec_B.flatten())
        pearson_list.append([[A, B], result_pearson])
    return_pearson_list = sorted(pearson_list, key=lambda x: x[1], reverse=True)[:10]
    return return_pearson_list

# ダイス係数の計算
def Dice(csv, A=None, B=None):
    dice_list = []
    if (B is None) and (A is not None):
        vec_A, vec_B = read_csv(csv, A-2)
        Vec_A = vec_A[0].reshape(1, -1)
        for k in range(len(vec_B)):
            if k == A-2:
                continue
            Vec_B = vec_B[k].reshape(1, -1)
            dice_list.append([[A, k+2], 1 - dice(Vec_A.flatten(), Vec_B.flatten())])
    elif (B is None) and (A is None):
        vec_A, vec_B = read_csv(csv)
        for n in range(len(vec_A)):
            for m in range(n, len(vec_B)):
                if n == m:
                    continue
                Vec_A = vec_A[n].reshape(1, -1)
                Vec_B = vec_B[m].reshape(1, -1)
                dice_list.append([[n+2, m+2], 1 - dice(Vec_A.flatten(), Vec_B.flatten())])
    else:
        vec_A, vec_B = read_csv(csv, A-2, B-2)
        Vec_A = vec_A[0].reshape(1, -1)
        Vec_B = vec_B[0].reshape(1, -1)
        dice_list.append([[A, B], 1 - dice(Vec_A.flatten(), Vec_B.flatten())])
    sorted_dice_list = sorted(dice_list, key=lambda x: x[1], reverse=True)[:10]
    return sorted_dice_list

# KLダイバージェンスの計算
def Kl(csv, A=None, B=None):
    kl_list = []
    if (B is None) and (A is not None):
        vec_A, vec_B = read_csv(csv, A-2)
        Vec_A = vec_A[0].reshape(1, -1)
        for k in range(len(vec_B)):
            if k == A-2:
                continue
            Vec_B = vec_B[k].reshape(1, -1)
            kl_list.append([[A, k+2], np.sum(rel_entr(Vec_A.flatten() / np.sum(Vec_A), Vec_B.flatten() / np.sum(Vec_B)))])
    elif (B is None) and (A is None):
        vec_A, vec_B = read_csv(csv)
        for n in range(len(vec_A)):
            for m in range(n, len(vec_B)):
                if n == m:
                    continue
                Vec_A = vec_A[n].reshape(1, -1)
                Vec_B = vec_B[m].reshape(1, -1)
                kl_list.append([[n+2, m+2], np.sum(rel_entr(Vec_A.flatten() / np.sum(Vec_A), Vec_B.flatten() / np.sum(Vec_B)))])
    else:
        vec_A, vec_B = read_csv(csv, A-2, B-2)
        Vec_A = vec_A[0].reshape(1, -1)
        Vec_B = vec_B[0].reshape(1, -1)
        kl_list.append([[A, B], np.sum(rel_entr(Vec_A.flatten() / np.sum(Vec_A), Vec_B.flatten() / np.sum(Vec_B)))])
    sorted_kl_list = sorted(kl_list, key=lambda x: x[1])[:10]
    return sorted_kl_list

def main():
    if __name__ == "__main__":
        main()