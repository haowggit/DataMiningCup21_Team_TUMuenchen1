from preprocessing import *
from AutoEncoder import *
from sklearn.model_selection import train_test_split


if __name__ == '__main__':

    sparse_data = scipy.sparse.load_npz('OHE_sparse_matrix.npz')


    train_data, val_data = train_test_split(sparse_data, test_size=0.1, random_state=42)
    indices = np.arange(train_data.shape[0])
    np.random.shuffle(indices)
    train_data = train_data[list(indices)]

    indices = np.arange(val_data.shape[0])
    np.random.shuffle(indices)
    val_data = val_data[list(indices)]

    train_dataset = SparseDataset(train_data)
    train_dataloader = DataLoader(train_dataset,
                          batch_size=4000, shuffle= False,
                          collate_fn=sparse_batch_collate)
    val_dataset = SparseDataset(train_data)
    val_dataloader = DataLoader(val_dataset,
                          batch_size=4000,
                          collate_fn=sparse_batch_collate)

    device = 'cuda'
    ae = AutoEncoder(n_latent= 50, n_init = sparse_data.shape[1])
    Loss = nn.MSELoss()
    # nn.MSELoss()
    # nn.BCEWithLogitsLoss()
    # DiceLoss()
    # nn.CosineEmbeddingLoss(reduction='none')
    # nn.CrossEntropyLoss()
    train(ae, train_dataloader, val_dataloader, lr = 1e-03, EPOCHES = 10,
          Loss = Loss, use_sparsity= False, device = device)