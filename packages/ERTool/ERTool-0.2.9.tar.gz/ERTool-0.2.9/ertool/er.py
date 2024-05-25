import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

np.set_printoptions(suppress=True)

def yager_rule(DBF, numOfEvidence, numOfPropositions):
    """
    Input Variables:
        - DBF: A two-dimensional array of floats. It stands for "Degrees of Belief" and is one of the main inputs to the algorithm, used to represent the initial belief degree of each proposition supported by each evidence.
        - numOfEvidence: An integer. It indicates the number of evidence to be combined. In the DBF array, this typically corresponds to the number of rows.
        - numOfPropositions: An integer. It indicates the number of propositions or evidential grades. In the DBF array, this typically corresponds to the number of columns.
    Output Values:
        - B Array: Upon completion of the Yager's Rule, the B array is updated with the final calculation results. It reflects the degree of belief of each proposition or evidential grades for the object being assessed after combining all available evidence. The pre-Numofproposition values in the B represent the belief degree of each proposition after evidence fusion. The last value of the B represents the belief degree of the global uncertainty.
        - False (Boolean): It returns True if the algorithm successfully executes and completes all computations. If any error is encountered during execution (e.g., division by zero), it returns False.
    """
    def yager_combination_2(m1, m2):
        def conflict_measure(m1, m2):
            K = 0
            for A in m1:
                for B in m2:
                    if not (A == B):
                        K += m1[A] * m2[B]
            return K

        def combined_mass(m1, m2, K):
            combined = {}
            for A in m1:
                for B in m2:
                    if A == B:
                        intersection = A
                        if intersection:
                            combined[intersection] = combined.get(intersection, 0) + m1[A] * m2[B]

            combined['Global Uncertainty'] = K
            return combined

        K = conflict_measure(m1, m2)
        return combined_mass(m1, m2, K)

    def DBP2Mlist(DBF,P = None):
        if P:
            Mlist = [ {P[j]:i[j] for j in range(len(DBF[0]))} for i in DBF]
        else:
            P = ['Proposition ' + str(i+1) for i in range(len(DBF[0]))]
            Mlist = [ {P[j]:i[j] for j in range(len(DBF[0]))} for i in DBF]
        return Mlist

    if len(DBF) != numOfEvidence or len(DBF[0]) != numOfPropositions or numOfEvidence < 1 or numOfPropositions < 1:
        print("An error occurred during the execution of the algorithm.")
        print(" | The input variables are incorrect. Please check them again. | ")
        return False

    Mlist = DBP2Mlist(DBF)
    ma = Mlist[0]
    mb = Mlist[1]
    for i in range(1,len(Mlist)-1):
        ma = yager_combination_2(ma,mb)
        ma.pop('Global Uncertainty')
        mb = Mlist[i+1]
    result = yager_combination_2(ma,mb)
    result.pop('Global Uncertainty')
    result['Global Uncertainty'] = 1 - sum(result.values())
    return list(result.values())

def murphy_rule(DBF,numOfEvidence,numOfPropositions):
    """
    Input Variables:
        - DBF: A two-dimensional array of floats. It stands for "Degrees of Belief" and is one of the main inputs to the algorithm, used to represent the initial belief degree of each proposition supported by each evidence.
        - numOfEvidence: An integer. It indicates the number of evidence to be combined. In the DBF array, this typically corresponds to the number of rows.
        - numOfPropositions: An integer. It indicates the number of propositions or evidential grades. In the DBF array, this typically corresponds to the number of columns.
    Output Values:
        - B Array: Upon completion of the Murphy's Rule, the B array is updated with the final calculation results. It reflects the degree of belief of each proposition or evidential grades for the object being assessed after combining all available evidence. The pre-Numofproposition values in the B represent the belief degree of each proposition after evidence fusion. The last value of the B represents the belief degree of the global uncertainty.
        - False (Boolean): It returns True if the algorithm successfully executes and completes all computations. If any error is encountered during execution (e.g., division by zero), it returns False.
    """
    
    if len(DBF) != numOfEvidence or len(DBF[0]) != numOfPropositions or numOfEvidence < 1 or numOfPropositions < 1:
        print("An error occurred during the execution of the algorithm.")
        print(" | The input variables are incorrect. Please check them again. | ")
        return False
    Mave = DBF.mean(axis=0)
    M = dempster_rule([Mave,Mave],numOfEvidence=2,numOfPropositions=numOfPropositions)
    for i in range(numOfEvidence-2):
        M = dempster_rule([M[:-1],Mave],numOfEvidence=2,numOfPropositions=numOfPropositions)
    return M


def er_algorithm(W, DBF, numOfEvidence, numOfPropositions,round = 4):
    """
    Input Variables:
        - W: A one-dimensional array of floats. It represents the weights of each piece of evidence. These weights are used in the algorithm to adjust the influence of each evidence.
        - DBF: A two-dimensional array of floats. It stands for "Degrees of Belief" and is one of the main inputs to the algorithm, used to represent the initial belief degree of each proposition supported by each evidence.
        - numOfEvidence: An integer. It indicates the number of evidence to be combined. In the DBF array, this typically corresponds to the number of rows.
        - numOfPropositions: An integer. It indicates the number of propositions or evidential grades. In the DBF array, this typically corresponds to the number of columns.
        - round: An integer. It indicates how many decimal places are retained in the final result, the default value is 4.
    Output Values:
        - B Array: Upon completion of the algorithm, the B array is updated with the final calculation results. It reflects the degree of belief of each proposition or evidential grades for the object being assessed after combining all available evidence. The pre-Numofproposition values in the B represent the belief degree of each proposition after evidence fusion. The last value of the B represents the belief degree of the global uncertainty.
        - False (Boolean): It returns True if the algorithm successfully executes and completes all computations. If any error is encountered during execution (e.g., division by zero), it returns False.
    """
    # 对输入进行检测
    if len(DBF) != numOfEvidence or len(DBF[0]) != numOfPropositions or numOfEvidence < 1 or numOfPropositions < 1:
        print("An error occurred during the execution of the algorithm.")
        print(" | The input variables are incorrect. Please check them again. | ")
        return False
    
    # 将数组转换为 numpy array
    if not isinstance(W, np.ndarray):
        W = np.array(W)
    if not isinstance(DBF, np.ndarray):
        DBF = np.array(DBF)

    # 归一化 W 数组
    sngSum = W.sum()
    if sngSum == 0:
        strErrorMessage += " | Divided by 0 (sngSum) in er_algorithm. | "
    else:
        W  = W / sngSum

    # 初始化变量
    B = np.zeros(numOfPropositions+1)
    strErrorMessage = ""
    MTilde = numOfPropositions
    MBar = numOfPropositions + 1
    ng2 = numOfPropositions + 2

    # 创建一个二维数组 M
    M = np.zeros((numOfEvidence, ng2), dtype=float)

    # 将 DBF 数组赋值到 M 矩阵
    for i in range(numOfEvidence):
        for j in range(numOfPropositions):
            M[i, j] = DBF[i, j]

    # 计算概率分布的不完备因子
    for i in range(numOfEvidence):
        sngIncomplete = np.sum(M[i, :numOfPropositions])
        M[i, MTilde] = W[i] * (1.0 - sngIncomplete)  # m(theta,i)
        M[i, MBar] = 1.0 - W[i]  # m(P(theta),i)

    # 利用权重更新 M 矩阵中的概率分配
    for i in range(numOfEvidence):
        for j in range(numOfPropositions):
            M[i, j] *= W[i]

    # 赋初值
    B[:numOfPropositions] = M[0, :numOfPropositions]
    B[MTilde] = M[0, MTilde]
    BBar = M[0, MBar]

    # 递归地融合所有evidence，并根据概率分配不完备因子和权重因子
    for r in range(1, numOfEvidence):
        K = 1.0 - np.sum([B[i] * M[r, j] for i in range(numOfPropositions) for j in range(numOfPropositions) if j != i])
        if K != 0:
            K = 1.0 / K
        else:
            strErrorMessage += " | Divided by 0 (K) in er_algorithm. | "

        for n in range(numOfPropositions):
            B[n] = K * (B[n] * M[r, n] + B[n] * (M[r, MTilde] + M[r, MBar]) + (B[MTilde] + BBar) * M[r, n])

        B[MTilde] = K * (B[MTilde] * M[r, MTilde] + BBar * M[r, MTilde] + B[MTilde] * M[r, MBar])
        BBar = K * BBar * M[r, MBar]

    # 归一化置信度
    sngNormal = 1.0 - BBar
    if sngNormal != 0:
        B /= sngNormal
    else:
        strErrorMessage += " | Divided by 0 (sngNormal) in er_algorithm. | "

    # 检查是否有错误信息
    if strErrorMessage:
        print("An error occurred during the execution of the algorithm.")
        print(strErrorMessage)
        return False
    else:
        return [x.round(round) for x in B]

def dempster_rule(DBF, numOfEvidence, numOfPropositions):
    """
    Input Variables:
        - DBF: A two-dimensional array of floats. It stands for "Degrees of Belief" and is one of the main inputs to the algorithm, used to represent the initial belief degree of each proposition supported by each evidence.
        - numOfEvidence: An integer. It indicates the number of evidence to be combined. In the DBF array, this typically corresponds to the number of rows.
        - numOfPropositions: An integer. It indicates the number of propositions or evidential grades. In the DBF array, this typically corresponds to the number of columns.
    Output Values:
        - B Array: Upon completion of the Dempster's Rule, the B array is updated with the final calculation results. It reflects the degree of belief of each proposition or evidential grades for the object being assessed after combining all available evidence. The pre-Numofproposition values in the B represent the belief degree of each proposition after evidence fusion. The last value of the B represents the belief degree of the global uncertainty.
        - False (Boolean): It returns True if the algorithm successfully executes and completes all computations. If any error is encountered during execution (e.g., division by zero), it returns False.
    """
    if len(DBF) != numOfEvidence or len(DBF[0]) != numOfPropositions or numOfEvidence < 1 or numOfPropositions < 1:
        print("An error occurred during the execution of the algorithm.")
        print(" | The input variables are incorrect. Please check them again. | ")
        return False
    
    B = np.zeros(numOfPropositions+1)
    
    if not isinstance(DBF, np.ndarray):
        DBF = np.array(DBF)

    W = [1] * numOfEvidence

    strErrorMessage = ""
    MTilde = numOfPropositions
    MBar = numOfPropositions + 1
    ng2 = numOfPropositions + 2

    M = np.zeros((numOfEvidence, ng2), dtype=float)

    for i in range(numOfEvidence):
        for j in range(numOfPropositions):
            M[i, j] = DBF[i, j]

    for i in range(numOfEvidence):
        sngIncomplete = np.sum(M[i, :numOfPropositions])
        M[i, MTilde] = W[i] * (1.0 - sngIncomplete)
        M[i, MBar] = 1.0 - W[i]

    for i in range(numOfEvidence):
        for j in range(numOfPropositions):
            M[i, j] *= W[i]

    B[:numOfPropositions] = M[0, :numOfPropositions]
    B[MTilde] = M[0, MTilde]
    BBar = M[0, MBar]

    for r in range(1, numOfEvidence):
        K = 1.0 - np.sum([B[i] * M[r, j] for i in range(numOfPropositions) for j in range(numOfPropositions) if j != i])
        if K != 0:
            K = 1.0 / K
        else:
            strErrorMessage += " | Divided by 0 (K) in er_algorithm. | "

        for n in range(numOfPropositions):
            B[n] = K * (B[n] * M[r, n] + B[n] * (M[r, MTilde] + M[r, MBar]) + (B[MTilde] + BBar) * M[r, n])

        B[MTilde] = K * (B[MTilde] * M[r, MTilde] + BBar * M[r, MTilde] + B[MTilde] * M[r, MBar])
        BBar = K * BBar * M[r, MBar]

    sngNormal = 1.0 - BBar
    if sngNormal != 0:
        B /= sngNormal
    else:
        strErrorMessage += " | Divided by 0 (sngNormal) in er_algorithm. | "

    if strErrorMessage:
        print("An error occurred during the execution of the algorithm.")
        print(strErrorMessage)
        return False
    else:
        return [x for x in B]
    
    
def show_er_result_origin(B, P = None, fig_name = "Visualization of the ER-based calculation results", xlabel_name = "Propositions", ylabel_name = "Belief Degree"):
    if P is None:
        P = ["Proposition "+str(i) for i in range(1,len(B))]
    P = P + ["Global Uncertainty"]
    # 创建柱状图
    plt.figure(figsize=(10, 6))
    bars = plt.bar(P, B, color = plt.get_cmap('Pastel1')(range(len(P))))

    # 添加标题和标签
    plt.title(fig_name, fontsize=14)
    plt.xlabel(xlabel_name, fontsize=12)
    plt.ylabel(ylabel_name, fontsize=12)

    # 设置y轴的范围
    plt.ylim(0, 1)

    # 为每个条形图添加数值标签
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 4), ha='center', va='bottom', fontsize=10)

    # 显示图表
    plt.show()

def show_er_result(B, P = None, fig_name="Visualization of the ER-based calculation results", xlabel_name="Propositions", ylabel_name="Belief Degree", dpi=300):
    if P is None:
        P = ["Proposition "+str(i) for i in range(1,len(B))]
    P = P + ["Global Uncertainty"]
    
    # 设置图表样式和字体
    plt.style.use('seaborn-whitegrid')  # 使用Seaborn的白色网格样式
    plt.rcParams['font.family'] = 'Helvetica'  # 设置字体为Helvetica
    plt.rcParams['text.color'] = 'black'
    plt.rcParams['axes.labelcolor'] = 'black'
    plt.rcParams['xtick.color'] = 'black'
    plt.rcParams['ytick.color'] = 'black'
    
    # 创建柱状图，并设置dpi提高图像分辨率
    plt.figure(figsize=(10, 6), dpi=dpi)
    bars = plt.bar(P, B, color=sns.color_palette("crest_r", len(P)), edgecolor='black')
    
    # 添加标题和标签
    plt.title(fig_name, fontsize=14, color='black', fontweight='bold')
    plt.xlabel(xlabel_name, fontsize=12)
    plt.ylabel(ylabel_name, fontsize=12)
    
    # 设置y轴的范围
    plt.ylim(0, 1)
    
    # 为每个条形图添加数值标签
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 4), ha='center', va='bottom', fontsize=10, color='black')
    
    # 关闭背景网格
    plt.grid(False)
    
    # 显示图表
    plt.show()

def run_algorithm_from_file(file_path, algorithm = 'ER', fig_name = "Visualization of the ER-based calculation results", xlabel_name = "Propositions", ylabel_name = "Belief Degree"):
    '''
    Input Variables:
        - file_path: A string. The address of the csv or xlsx file. Note that the format of data strictly follows the format of the template.
        - algorithm: 'ER' or 'DS'. ER' stands for using the evidence inference algorithm, and 'DS' stands for using the Dempster-Shafer algorithm.
    Output Values:
        - B Array: Upon completion of the algorithm, the B array is updated with the final calculation results. It reflects the degree of belief of each proposition or evidential grades for the object being assessed after combining all available evidence. The pre-Numofproposition values in the B represent the belief degree of each proposition after evidence fusion. The last value of the B represents the belief degree of the global uncertainty.
        - False (Boolean): It returns True if the algorithm successfully executes and completes all computations. If any error is encountered during execution (e.g., division by zero), it returns False.
    '''
    # 根据文件扩展名决定使用的读取方法
    _, file_extension = os.path.splitext(file_path)
    if file_extension.lower() == '.csv':
        df = pd.read_csv(file_path)
    elif file_extension.lower() == '.xlsx':
        df = pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Please provide a .csv or .xlsx file.")
    
    # ER算法
    if algorithm == 'ER':
        # 计算numOfEvidence和numOfPropositions
        numOfEvidence = len(df)
        numOfPropositions = len(df.columns) - 2

        # 提取DBF矩阵
        DBF = df.iloc[:, 2:].to_numpy()

        # 提取W数组
        W = df['Weight'].to_numpy()

        # 提取P数组
        P = df.columns[2:].tolist()

        # 调用函数
        B = er_algorithm(W, DBF, numOfEvidence, numOfPropositions)

    # dempster_rule算法
    elif algorithm == 'DS':
        # 计算numOfEvidence和numOfPropositions
        numOfEvidence = len(df)
        numOfPropositions = len(df.columns) - 2

        # 提取DBF矩阵
        DBF = df.iloc[:, 2:].to_numpy()

        # 提取P数组
        P = df.columns[2:].tolist()

        # 调用函数
        B = dempster_rule(DBF, numOfEvidence, numOfPropositions)

    if B is not None:
        show_er_result(B, P, fig_name, xlabel_name, ylabel_name)

    return B

def single_combine(fold_path, algorithm='ER'):
    """
    Enter the folder address XX and merge the evidence from XXX_tobecombined.csv under this folder.
    Output the B array.
    """
    # 构建文件路径
    file_name = os.path.basename(fold_path) + '_tobecombined.csv'
    file_path = os.path.join(fold_path, file_name)
    
    # 检查文件是否存在
    if not os.path.exists(file_path):
        print("The _tobecombined.csv file does not exist:", file_path)
        return None
    
    # 根据指定的算法调用相应的函数处理文件
    
    # 假设run_algorithm_from_file是之前定义的函数，用于处理文件并应用ER算法
    result = run_algorithm_from_file(file_path,algorithm=algorithm)
    if result is not None:
        return result
    else:
        return None

def write_file(fold_path, B):
    """
    Enter the address of the folder XX and B, and fill B into the XXX_combined.csv file in this folder.
    """
    file_name = os.path.basename(fold_path) + '_combined.csv'
    file_path = os.path.join(fold_path, file_name)
    
    # 检查文件是否存在
    if os.path.exists(file_path):
        # 读取CSV文件
        df = pd.read_csv(file_path)
        
        # 确保数组B的长度与DataFrame的列数匹配（除了第一个和最后一个列）
        if len(B) - 1 != len(df.columns) - 2:
            print("B The length of the array does not match the number of columns in the CSV file.")
            return
        
        # 更新DataFrame的相应列，不包括B数组的最后一个元素
        for i in range(len(B) - 1):
            df.iloc[0, i + 2] = B[i]  # 更新第一行（索引为0），从第二列开始的值
        
        # 保存修改后的DataFrame回CSV
        df.to_csv(file_path, index=False)
        print(f"The _combined.csv file has been updated: {file_path}")
    else:
        print("The _combined.csv file does not exist:", file_path)
        return None
    
def single(fold_path, algorithm='ER'):
    """
    Enter the folder address, read the _tobecombined.csv file to do the evidence fusion in a single folder, and update the _combined.csv file under that folder.
    """
    B = single_combine(fold_path, algorithm=algorithm)
    write_file(fold_path,B)

def merge_csv_files(files, output_file):
    """
    Enter the files file address array, perform a csv merge, and output a new csv file.
    """
    combined_df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)
    combined_df.to_csv(output_file, index=False)

def merge_attribute(folder_path):
    """
    Enter a folder address to merge the _combined.csv file in all subfolders under that folder.
    """
    # 检查是否存在子文件夹
    if any(os.path.isdir(os.path.join(folder_path, d)) for d in os.listdir(folder_path)):
        combined_files = []
        for subdir in os.listdir(folder_path):
            subdir_path = os.path.join(folder_path, subdir)
            if os.path.isdir(subdir_path):
                combined_file = os.path.join(subdir_path, subdir + '_combined.csv')
                if os.path.exists(combined_file):
                    combined_files.append(combined_file)
        
        if combined_files:
            output_file = os.path.join(folder_path, os.path.basename(folder_path) + '_tobecombined.csv')
            merge_csv_files(combined_files, output_file)
            print(f"The merge is complete and the file is generated: {output_file}")
        else:
            print(f"Did not find any mergable files in {folder_path}")
    else:
        print(f"There are no subfolders under {folder_path}, return None.")
        return None

def print_directory_tree(startpath):
    """
    Print the directory tree structure starting from startpath.
    """
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f'{indent}{os.path.basename(root)}/')
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(f'{subindent}{f}')

def process_folder(folder_path,algorithm='ER'):
    """
    Recursively processes a given folder by first processing all subfolders and then the current folder.
    """
    # 确保当前路径是一个文件夹
    if not os.path.isdir(folder_path):
        print(f"{folder_path} is not a valid folder path.")
        return

    # 遍历当前文件夹的所有项
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        # 如果是文件夹，递归调用process_folder处理该文件夹
        if os.path.isdir(item_path):
            process_folder(item_path,algorithm=algorithm)

    # 处理当前文件夹
    # 检查是否为叶子节点文件夹（即不包含任何子文件夹）
    if not any(os.path.isdir(os.path.join(folder_path, d)) for d in os.listdir(folder_path)):
        # 如果是叶子节点文件夹，则调用single函数处理
        single(folder_path,algorithm=algorithm)
    else:
        # 如果不是叶子节点文件夹，则调用merge_attribute函数处理
        merge_attribute(folder_path)
        single(folder_path,algorithm=algorithm)

def multi_level_multi_source_2(fold_path,algorithm='ER'):
    """
    Recursively processes a given folder by first processing all subfolders and then the current folder.
    """
    try:
        process_folder(fold_path,algorithm=algorithm)
        print("OK!")
    except Exception as e:
        print(f"An error occurred during processing: {e}")
        
def extract_leaf_fold(fold_path):
    result = []  # 存储最终结果的列表
    objects_data = {}  # 存储每个Objects名字对应的数据
    
    for file in os.listdir(fold_path):
        if file.endswith('.csv') and not file.endswith('_combined.csv'):
            df = pd.read_csv(os.path.join(fold_path, file))
            for index, row in df.iterrows():
                obj_name = row['Objects']
                if obj_name not in objects_data:
                    objects_data[obj_name] = pd.DataFrame(columns=df.columns)
                # 修改这里，使用pd.concat来添加行数据
                objects_data[obj_name] = pd.concat([objects_data[obj_name], pd.DataFrame([row])], ignore_index=True)
    
    for obj_name, df in objects_data.items():
        result.append(df)
    
    return result

def combine_df(df):
    # 提取Weight列的数据
    W = df['Weight'].to_list()
    
    # 构建二维数组DBFM
    DBFM = df.iloc[:, 3:].values.tolist()  # 从第四列开始到最后一列的数据
    
    # 定义变量
    numOfEvidence = len(df)
    numOfPropositions = len(df.columns) - 3  # 减去前三列
    
    # 调用er_algorithm函数
    B = er_algorithm(W, DBFM, numOfEvidence, numOfPropositions)
    
    # 返回B数组的前numOfPropositions个元素组成的数组
    return B[:numOfPropositions]

def write_csv(df_list, csv_path):
    # 检查文件是否存在
    if not os.path.exists(csv_path):
        print(f"File {csv_path} does not exist.")
        return None
    
    # 读取原有CSV文件
    original_df = pd.read_csv(csv_path)
    
    for df in df_list:
        # 对每个dataframe调用combine_df(df)
        B = combine_df(df)
        
        # 获取Objects列的第一个值
        obj_value = df['Objects'].iloc[0]
        
        # 查找对应的行索引
        row_index = original_df[original_df['Objects'] == obj_value].index
        
        if not row_index.empty:
            # 从第4列开始更新B数组的值
            for i, value in enumerate(B, start=3):  # 注意列索引从0开始，所以从第4列开始是索引3
                original_df.at[row_index[0], original_df.columns[i]] = value
    
    # 写回CSV文件
    original_df.to_csv(csv_path, index=False)
    print(f"Updated CSV file saved to {csv_path}.")
    
def combine_leaf_fold(fold_path):
    """combine leaf fold
    Args:
        fold_path (_type_): _description_
    """
    result = extract_leaf_fold(fold_path)
    for file in os.listdir(fold_path):
        if file.endswith('_combined.csv'):
            csv_path = os.path.join(fold_path, file)
            # csv_path = fold_path+"/"+file
            write_csv(result, csv_path)

def combine_not_leaf_fold(folder_path):
    """
    Enter a folder address to merge the _combined.csv file in all subfolders under that folder.
    """

    # 检查是否存在子文件夹
    if any(os.path.isdir(os.path.join(folder_path, d)) for d in os.listdir(folder_path)):
        combined_files = []
        for subdir in os.listdir(folder_path):
            subdir_path = os.path.join(folder_path, subdir)
            if os.path.isdir(subdir_path):
                combined_file = os.path.join(subdir_path, subdir + '_combined.csv')
                if os.path.exists(combined_file):
                    combined_files.append(combined_file)
        # print(combined_files)
        
        result = []  # 存储最终结果的列表
        objects_data = {}  # 存储每个Objects名字对应的数据
        for f in combined_files:
            df = pd.read_csv(f)
            for index, row in df.iterrows():
                obj_name = row['Objects']
                if obj_name not in objects_data:
                    objects_data[obj_name] = pd.DataFrame(columns=df.columns)
                # 修改这里，使用pd.concat来添加行数据
                objects_data[obj_name] = pd.concat([objects_data[obj_name], pd.DataFrame([row])], ignore_index=True)
            
        for obj_name, df in objects_data.items():
            result.append(df)
            
        # print(os.listdir(folder_path))
        for file in os.listdir(folder_path):
            if file.endswith('_combined.csv'):
                csv_path = folder_path+"/"+file
                write_csv(result, csv_path)
        
    else:
        print(f"There are no subfolders under {folder_path}, return None.")
        return None

def combine_folder(folder_path):
    """
    Recursively processes a given folder by first processing all subfolders and then the current folder.
    """
    # 确保当前路径是一个文件夹
    if not os.path.isdir(folder_path):
        print(f"{folder_path} is not a valid folder path.")
        return None

    # 遍历当前文件夹的所有项
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        # 如果是文件夹，递归调用process_folder处理该文件夹
        if os.path.isdir(item_path):
            combine_folder(item_path)

    # 处理当前文件夹
    # 检查是否为叶子节点文件夹（即不包含任何子文件夹）
    if not any(os.path.isdir(os.path.join(folder_path, d)) for d in os.listdir(folder_path)):
        # 如果是叶子节点文件夹，则调用single函数处理
        combine_leaf_fold(folder_path)
    else:
        # 如果不是叶子节点文件夹，则调用merge_attribute函数处理
        combine_not_leaf_fold(folder_path)
        
def root_file_1(file_path):
    try:
        # 读取CSV文件
        df = pd.read_csv(file_path)
        
        # 在第一列后插入一列Weight，值都为1
        df.insert(0, 'Weight', 1)
        
        # 将第一列复制并放在最前面，列名改为Objects
        df.insert(0, 'Objects', df.iloc[:, 1])
        
        # 保存修改后的CSV文件
        df.to_csv(file_path, index=False)
        
        print("Done1!")
    except FileNotFoundError:
        print("The file does not exist.")


def root_file_2(file_path):
    try:
        df = pd.read_csv(file_path)
        df.drop(df.columns[[0, 1]], axis=1, inplace=True)
        df.to_csv(file_path, index=False)     
        print("Done2!")
    except FileNotFoundError:
        print("The file does not exist.")

def multi_level_multi_source(folder_path):
    """
    Recursively processes a given folder by first processing all subfolders and then the current folder.
    """
    try:
        root_file_1(os.path.join(folder_path,"Objects_combined.csv"))
        combine_folder(folder_path)
        root_file_2(os.path.join(folder_path,"Objects_combined.csv"))
        print("OK!")
    except Exception as e:
        print(f"An error occurred during processing: {e}")