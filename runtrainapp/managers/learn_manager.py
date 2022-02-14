# Setup
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay
from matplotlib import pyplot as plt
from joblib import dump, load
from ..utils.constants import *
import os


# Utilities methods
# Cosmetic function to print break line
def break_line():
    print('-------------------------------------------------------------------------------')


# Cosmetic function to print empty line
def break_empty():
    print()


# Model creation general methods
# Create, train Decision Tree model and measure accuracy
# Default 10% of data (0.1) - for testing
def decision_tree_fit_and_measure(X, y, test_size=0.1):
    # Split dataframe for Training and Testing
    X_trn, X_tst, y_trn, y_tst = train_test_split(X, y, test_size=test_size)

    # Create first model before first iteration
    model = DecisionTreeClassifier()
    # Train model
    model.fit(X_trn, y_trn)
    # Make predictions basing on Input testing data
    predictions = model.predict(X_tst)
    # Measure accuracy
    score = accuracy_score(y_tst, predictions)

    return {
        'model': model,
        'predictions': predictions,
        'score': score,
        'X_trn': X_trn,
        'X_tst': X_tst,
        'y_trn': y_trn,
        'y_tst': y_tst
    }


# Create, train Linear Regression model and measure accuracy
# Default 10% of data (0.1) - for testing
def linear_reg_fit_and_measure(X, y, test_size=0.1):
    # Split dat aframe for Training and Testing
    X_trn, X_tst, y_trn, y_tst = train_test_split(X, y, test_size=test_size)

    # Create and train model
    model = LinearRegression()
    model.fit(X_trn, y_trn)
    # Make predictions basing on Input testing data
    predictions = model.predict(X_tst)
    # Measure accuracy
    score = model.score(X_tst, y_tst)

    # Flat array of arrays (result of predict)
    predictions = predictions.flatten()
    # Predictions cannot be float - rounding and casting to float
    predictions = np.around(predictions)
    predictions = predictions.astype(int)

    return {
        'model': model,
        'predictions': predictions,
        'score': score,
        'X_trn': X_trn,
        'X_tst': X_tst,
        'y_trn': y_trn,
        'y_tst': y_tst
    }


# Create, train K Neighbors Regressor model and measure accuracy
# Default 10% of data (0.1) - for testing
def k_neigh_reg_fit_and_measure(X, y, test_size=0.1):
    # Split dataframe for Training and Testing
    X_trn, X_tst, y_trn, y_tst = train_test_split(X, y, test_size=test_size)

    # Create first model before first iteration
    model = KNeighborsRegressor()
    # Train model
    model.fit(X_trn, y_trn)
    # Make predictions basing on Input testing data
    predictions = model.predict(X_tst)
    # Measure accuracy
    score = model.score(X_tst, y_tst)

    # Flat array of arrays (result of predict)
    predictions = predictions.flatten()
    # Predictions cannot be float - rounding and casting to float
    predictions = np.around(predictions)
    predictions = predictions.astype(int)

    return {
        'model': model,
        'predictions': predictions,
        'score': score,
        'X_trn': X_trn,
        'X_tst': X_tst,
        'y_trn': y_trn,
        'y_tst': y_tst
    }


# Model persistence methods
# Get current dir path and add models
def get_models_path():
    current_path = os.getcwd()
    models_dir_path = current_path + '/form_data/models/'

    return models_dir_path


# Get current dir path and add plots
def get_plots_path():
    current_path = os.getcwd()
    plots_dir_path = current_path + '/form_data/plots/'

    return plots_dir_path


# Create models dir if not exists
def create_models_dir():
    path = get_models_path()
    is_exist = os.path.exists(path)
    if not is_exist:
        print('Creating ' + path)
        os.makedirs(path)


# Create plots dir if not exists
def create_plots_dir():
    path = get_plots_path()
    is_exist = os.path.exists(path)
    if not is_exist:
        print('Creating ' + path)
        os.makedirs(path)


# Save model to file
def save_model_from_dict(model_dict, model_name):
    filename = model_name + '.joblib'
    model = model_dict['model']
    print('Saving ' + filename)
    dump(model, get_models_path() + filename)


# Read model from file
def get_model_from_file(model_name):
    filename = model_name + '.joblib'
    model = load(get_models_path() + filename)

    return model


# DecisionTreeClassifier Visualisation methods
# basing on data provided in dt_model_dict
# dt_model_name used for filenames and cosmetics
def visualise_dt_model_by_dict(dt_model_dict, dt_model_name, save_model=True):
    print('DecisionTreeClassifier ' + dt_model_name)
    break_line()

    # Print summary of DecisionTreeClassifier
    summary_dt_model_by_dict(dt_model_dict)

    print('Visualisation ' + str(dt_model_name))
    break_line()

    show_and_save_dt_plot(dt_model_dict, dt_model_name)
    show_and_save_dt_conf_matrix(dt_model_dict, dt_model_name)
    show_and_save_dt_tot_imp_vs_eff_alph(dt_model_dict, dt_model_name)

    if save_model:
        save_model_from_dict(dt_model_dict, dt_model_name)


# Print DecisionTreeClassifier summary
def summary_dt_model_by_dict(dt_model_dict):
    print('Model summary')
    break_line()

    dt_model = dt_model_dict['model']

    print('Model score:')
    print(dt_model_dict['score'])
    break_empty()

    print('Tree depth:')
    print(dt_model.get_depth())
    break_empty()

    print('Tree number of leaves:')
    print(dt_model.get_n_leaves())
    break_empty()


# Show and save DecisionTreeClassifier plot_tree
def show_and_save_dt_plot(dt_model_dict, dt_model_name):
    # DecisionTreeClassifier plot_tree
    print('DecisionTreeClassifier plot tree')
    # Turn off GUI Interactive Mode
    plt.ioff()
    # Plot size
    # # plt.figure(figsize=(35, 30))
    plot_tree(dt_model_dict['model'], filled=True)
    plt.title('Decision tree based on ' + dt_model_name)
    # Save plot to a file
    plt.savefig(get_plots_path() + dt_model_name + ' - plot tree.png')
    # Show plot
    # plt.show()
    # Clear plot
    plt.clf()


# Show and save DecisionTreeClassifier confusion matrix
def show_and_save_dt_conf_matrix(dt_model_dict, dt_model_name):
    # DecisionTreeClassifier confusion_matrix
    print('DecisionTreeClassifier confusion_matrix')
    # Turn off GUI Interactive Mode
    plt.ioff()
    # Create Confusion Matrix plot basing on test output and predictions
    ConfusionMatrixDisplay.from_predictions(dt_model_dict['y_tst'], dt_model_dict['predictions'])
    # Save plot to a file
    plt.savefig(get_plots_path() + dt_model_name + ' - confusion matrix.png')
    # Show plot
    #   plt.show()
    # Clear plot
    plt.clf()


# Show and save DecisionTreeClassifier Total impurity of leaves vs effective alphas plot
def show_and_save_dt_tot_imp_vs_eff_alph(dt_model_dict, dt_model_name):
    print('DecisionTreeClassifier Total impurity of leaves vs effective alphas')
    dt_model = dt_model_dict['model']
    # Turn off GUI Interactive Mode
    plt.ioff()
    # Plot size
    fig, ax = plt.subplots(figsize=(25, 20))
    # Calculate ccp_alphas and impurities
    dt_model_path = dt_model.cost_complexity_pruning_path(dt_model_dict['X_trn'], dt_model_dict['y_trn'])
    dt_model_ccp_alphas, dt_model_impurities = dt_model_path.ccp_alphas, dt_model_path.impurities
    # Create a plot
    ax.plot(dt_model_ccp_alphas[:-1], dt_model_impurities[:-1], marker="o", drawstyle="steps-post")
    ax.set_xlabel("Effective Alpha")
    ax.set_ylabel("Total Impurity of Leaves")
    ax.set_title("Total Impurity vs effective alpha for training set")
    # Save plot to a file
    plt.savefig(get_plots_path() + dt_model_name + ' - Total impurity of leaves vs effective alphas.png')
    # Show plot
    #   plt.show()
    # Clear plot
    plt.clf()


# LinearRegression Visualisation methods
# basing on data provided in lr_model_dict
# lr_model_name used for filenames and cosmetics
def visualise_lr_model_by_dict(lr_model_dict, lr_model_name, save_model=True):
    print('LinearRegression ' + lr_model_name)
    break_line()

    # Print summary of LinearRegression
    summary_lr_model_by_dict(lr_model_dict)

    print('Visualisation ' + str(lr_model_name))
    break_line()

    show_and_save_lr_pred_plot(lr_model_dict, lr_model_name)
    show_and_save_lr_conf_matrix(lr_model_dict, lr_model_name)

    if save_model:
        save_model_from_dict(lr_model_dict, lr_model_name)


# Print LinearRegression summary
def summary_lr_model_by_dict(lr_model_dict):
    print('Model summary')
    break_line()

    print('Model score:')
    print(lr_model_dict['score'])
    break_empty()


# Show and save LinearRegression predictions plot
def show_and_save_lr_pred_plot(lr_model_dict, lr_model_name):
    print('LinearRegression predictions plot')
    # Turn off GUI Interactive Mode
    plt.ioff()
    # Plot size
    # plt.figure(figsize=(25, 20))
    plt.plot(lr_model_dict['predictions'], "gd")
    plt.tick_params(axis="x", which="both", bottom=False, top=False, labelbottom=False)
    plt.ylabel("Predicted value")
    plt.xlabel("Training samples")
    plt.title('LinearRegression predictions from ' + lr_model_name)
    # Save plot to a file
    plt.savefig(get_plots_path() + lr_model_name + ' - predictions.png')
    # Show plot
    #   plt.show()
    # Clear plot
    plt.clf()


# Show and save LinearRegression confusion matrix
def show_and_save_lr_conf_matrix(lr_model_dict, lr_model_name):
    print('LinearRegression confusion_matrix')
    # Create Confusion Matrix plot basing on test output and predictions
    ConfusionMatrixDisplay.from_predictions(lr_model_dict['y_tst'], lr_model_dict['predictions'])
    # Turn off GUI Interactive Mode
    plt.ioff()
    # Save plot to a file
    plt.savefig(get_plots_path() + lr_model_name + ' - confusion matrix.png')
    # Show plot
    #   plt.show()
    # Clear plot
    plt.clf()


# KNeighborsRegressor Visualisation methods
# basing on data provided in knr_model_dict
# knr_model_name used for filenames and cosmetics
def visualise_knr_model_by_dict(knr_model_dict, knr_model_name, save_model=True):
    print('KNeighborsRegressor ' + knr_model_name)
    break_line()

    # Print summary of KNeighborsRegressor
    summary_lr_model_by_dict(knr_model_dict)

    print('Visualisation ' + str(knr_model_name))
    break_line()

    show_and_save_knr_pred_plot(knr_model_dict, knr_model_name)
    show_and_save_lr_conf_matrix(knr_model_dict, knr_model_name)

    if save_model:
        save_model_from_dict(knr_model_dict, knr_model_name)


# Print KNeighborsRegressor summary
def summary_lr_model_by_dict(knr_model_dict):
    print('Model summary')
    break_line()

    print('Model score:')
    print(knr_model_dict['score'])
    break_empty()


# Show and save KNeighborsRegressor predictions plot
def show_and_save_knr_pred_plot(knr_model_dict, knr_model_name):
    print('KNeighborsRegressor predictions plot')
    # Turn off GUI Interactive Mode
    plt.ioff()
    # Plot size
    # plt.figure(figsize=(25, 20))
    plt.plot(knr_model_dict['predictions'], "ys")
    plt.tick_params(axis="x", which="both", bottom=False, top=False, labelbottom=False)
    plt.ylabel("Predicted value")
    plt.xlabel("Training samples")
    plt.title('KNeighborsRegressor predictions from ' + knr_model_name)
    # Save plot to a file
    plt.savefig(get_plots_path() + knr_model_name + ' - predictions.png')
    # Show plot
    #   plt.show()
    # Clear plot
    plt.clf()


# Show and save KNeighborsRegressor confusion matrix
def show_and_save_knr_conf_matrix(knr_model_dict, knr_model_name):
    print('KNeighborsRegressor confusion_matrix')
    # Create Confusion Matrix plot basing on test output and predictions
    ConfusionMatrixDisplay.from_predictions(knr_model_dict['y_tst'], knr_model_dict['predictions'])
    # Turn off GUI Interactive Mode
    plt.ioff()
    # Save plot to a file
    plt.savefig(get_plots_path() + knr_model_name + ' - confusion matrix.png')
    # Show plot
    #   plt.show()
    # Clear plot
    plt.clf()


# Split df to distance specific dfs
def prepare_distance_dfs(df):
    # df for time 1km
    df_time_1km = df.loc[df['time_1km_id'] != 11]
    df_time_1km = df_time_1km.drop(columns=['time_5km_id', 'time_10km_id', 'time_21km_id', 'time_42km_id'])
    print('df_time_1km')
    break_line()
    print(df_time_1km)
    break_empty()

    # df for time 5km
    df_time_5km = df.loc[df['time_5km_id'] != 14]
    df_time_5km = df_time_5km.drop(columns=['time_1km_id', 'time_10km_id', 'time_21km_id', 'time_42km_id'])
    print('df_time_5km')
    break_line()
    print(df_time_5km)
    break_empty()

    # df for time 10km
    df_time_10km = df.loc[df['time_10km_id'] != 12]
    df_time_10km = df_time_10km.drop(columns=['time_1km_id', 'time_5km_id', 'time_21km_id', 'time_42km_id'])
    print('df_time_10km')
    break_line()
    print(df_time_10km)
    break_empty()

    # df for time 21km
    df_time_21km = df.loc[df['time_21km_id'] != 12]
    df_time_21km = df_time_21km.drop(columns=['time_1km_id', 'time_5km_id', 'time_10km_id', 'time_42km_id'])
    print('df_time_21km')
    break_line()
    print(df_time_21km)
    break_empty()

    # df for time 42km
    df_time_42km = df.loc[df['time_42km_id'] != 14]
    df_time_42km = df_time_42km.drop(columns=['time_1km_id', 'time_5km_id', 'time_10km_id', 'time_21km_id'])
    print('df_time_42km')
    break_line()
    print(df_time_42km)
    break_empty()

    return df_time_1km, df_time_5km, df_time_10km, df_time_21km, df_time_42km


# Split to X and y basing on distance column name
def split_X_y_by_distance_column(distance_df, distance_column_name):
    # Split data - Input (X) and Output (y)
    # X - Input Data
    X = distance_df.drop(columns=[distance_column_name])

    # y - Output data
    y = distance_df.filter([distance_column_name])

    return X, y


def learn_model():
    current_path = os.getcwd()
    # Default path
    file = current_path + '/form_data/Mapped - Ankieta dla biegaczy.csv'
    # Read csv file with responses
    df = pd.read_csv(file)

    # Drop additionally added column and id column
    df = df.drop(columns=['Unnamed: 0', 'id'])

    # Show the shape of dataframe (rows, columns)
    print('Form answer dataframe shape')
    break_line()
    print(df.shape)

    print('Form answer dataframe columns')
    break_line()
    for column in df.columns:
        print(column)

    df_time_1km, df_time_5km, df_time_10km, df_time_21km, df_time_42km = prepare_distance_dfs(df)

    # Execute directiories creation
    create_models_dir()
    create_plots_dir()

    # Dataframe df_time_1km
    # Training data with 1km time only
    # Split data - Input (X) and Output (y)
    # X - Input Data
    # y - Output data
    X_time_1km, y_time_1km = split_X_y_by_distance_column(df_time_1km, COLUMN_TIME_1KM_ID)

    # DecisionTreeClassifier
    dt_model_1km_dict = decision_tree_fit_and_measure(X_time_1km, y_time_1km)

    # LinearRegression
    lr_model_1km_dict = linear_reg_fit_and_measure(X_time_1km, y_time_1km)

    # KNeighborsRegressor
    knr_model_1km_dict = k_neigh_reg_fit_and_measure(X_time_1km, y_time_1km)

    # Visualisation df_time_1km models
    visualise_dt_model_by_dict(dt_model_1km_dict, DTM_MODEL_1KM)
    visualise_lr_model_by_dict(lr_model_1km_dict, LR_MODEL_1KM)
    visualise_knr_model_by_dict(knr_model_1km_dict, KNR_MODEL_1KM)

    # Dataframe df_time_5km
    # Training data with 5km time only
    # Split data - Input (X) and Output (y)
    # X - Input Data
    # y - Output data
    X_time_5km, y_time_5km = split_X_y_by_distance_column(df_time_5km, COLUMN_TIME_5KM_ID)

    # DecisionTreeClassifier
    dt_model_5km_dict = decision_tree_fit_and_measure(X_time_5km, y_time_5km)

    # LinearRegression
    lr_model_5km_dict = linear_reg_fit_and_measure(X_time_5km, y_time_5km)

    # KNeighborsRegressor
    knr_model_5km_dict = k_neigh_reg_fit_and_measure(X_time_5km, y_time_5km)

    # Visualisation df_time_5km models
    visualise_dt_model_by_dict(dt_model_5km_dict, DTM_MODEL_5KM)
    visualise_lr_model_by_dict(lr_model_5km_dict, LR_MODEL_5KM)
    visualise_knr_model_by_dict(knr_model_5km_dict, KNR_MODEL_5KM)

    # Dataframe df_time_10km
    # Training data with 10km time only
    # Split data - Input (X) and Output (y)
    # X - Input Data
    # y - Output data
    X_time_10km, y_time_10km = split_X_y_by_distance_column(df_time_10km, COLUMN_TIME_10KM_ID)

    # DecisionTreeClassifier
    dt_model_10km_dict = decision_tree_fit_and_measure(X_time_10km, y_time_10km)

    # LinearRegression
    lr_model_10km_dict = linear_reg_fit_and_measure(X_time_10km, y_time_10km)

    # KNeighborsRegressor
    knr_model_10km_dict = k_neigh_reg_fit_and_measure(X_time_10km, y_time_10km)

    # Visualisation df_time_10km models
    visualise_dt_model_by_dict(dt_model_10km_dict, DTM_MODEL_10KM)
    visualise_lr_model_by_dict(lr_model_10km_dict, LR_MODEL_10KM)
    visualise_knr_model_by_dict(knr_model_10km_dict, KNR_MODEL_10KM)

    # Dataframe df_time_21km
    # Training data with 21km time only
    # Split data - Input (X) and Output (y)
    # X - Input Data
    # y - Output data
    X_time_21km, y_time_21km = split_X_y_by_distance_column(df_time_21km, COLUMN_TIME_21KM_ID)

    # DecisionTreeClassifier
    dt_model_21km_dict = decision_tree_fit_and_measure(X_time_21km, y_time_21km)

    # LinearRegression
    lr_model_21km_dict = linear_reg_fit_and_measure(X_time_21km, y_time_21km)

    # KNeighborsRegressor
    knr_model_21km_dict = k_neigh_reg_fit_and_measure(X_time_21km, y_time_21km)

    # Visualisation df_time_21km models
    visualise_dt_model_by_dict(dt_model_21km_dict, DTM_MODEL_21KM)
    visualise_lr_model_by_dict(lr_model_21km_dict, LR_MODEL_21KM)
    visualise_knr_model_by_dict(knr_model_21km_dict, KNR_MODEL_21KM)

    # Dataframe df_time_42km
    # Training data with 42km time only
    # Split data - Input (X) and Output (y)
    # X - Input Data
    # y - Output data
    X_time_42km, y_time_42km = split_X_y_by_distance_column(df_time_42km, COLUMN_TIME_42KM_ID)

    # DecisionTreeClassifier
    dt_model_42km_dict = decision_tree_fit_and_measure(X_time_42km, y_time_42km)

    # LinearRegression
    lr_model_42km_dict = linear_reg_fit_and_measure(X_time_42km, y_time_42km)

    # KNeighborsRegressor
    knr_model_42km_dict = k_neigh_reg_fit_and_measure(X_time_42km, y_time_42km)

    # Visualisation df_time_42km models
    visualise_dt_model_by_dict(dt_model_42km_dict, DTM_MODEL_42KM)
    visualise_lr_model_by_dict(lr_model_42km_dict, LR_MODEL_42KM)
    visualise_knr_model_by_dict(knr_model_42km_dict, KNR_MODEL_42KM)
