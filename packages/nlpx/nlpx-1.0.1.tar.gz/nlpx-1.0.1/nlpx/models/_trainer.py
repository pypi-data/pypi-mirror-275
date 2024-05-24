import torch
from torch import nn, optim
from torch.utils.data import DataLoader, TensorDataset
from torch.optim.lr_scheduler import CosineAnnealingLR
from sklearn.model_selection import train_test_split


class Trainer:

	def __init__(self, model, train_set, eval_set, collate_fn=None,
				 max_iter=100, optimizer=optim.AdamW, learning_rate=0.001,
				 batch_size=8, eval_batch_size=16,
				 num_workers=4, num_eval_workers=2,
				 early_stopping_rounds=10,  # 早停，等10轮决策，评价指标不在变化，停止
				 device=torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')):
		self.model = model.to(device)
		self.train_loader = DataLoader(dataset=train_set, batch_size=batch_size,
									   num_workers=num_workers, shuffle=True, collate_fn=collate_fn)
		self.eval_loader = DataLoader(dataset=eval_set, batch_size=eval_batch_size,
									  num_workers=num_eval_workers, collate_fn=collate_fn)
		self.max_iter = max_iter
		self.optimizer = optimizer(model.parameters(), lr=learning_rate)
		self.early_stopping_rounds = early_stopping_rounds
		self.device = device

	def train(self):
		cnt = 0
		cnt2 = 0
		best_acc = 0.0
		last_acc = 0.0
		best_model = None
		scheduler = CosineAnnealingLR(self.optimizer, T_max=5, eta_min=0)
		for epoch in range(self.max_iter):
			total = 0.0
			losses = 0.0
			correct = 0.0
			self.model.train()
			for x, y in self.train_loader:
				x, y = x.to(self.device), y.to(self.device)
				loss, logits = self.model(x, y)
				self.optimizer.zero_grad()
				loss.backward()
				self.optimizer.step()
				scheduler.step()

				losses += loss.item()
				correct += (logits.argmax(1) == y).sum().item()
				total += len(y)

			val_loss, val_acc = self.eval()
			print('epoch-{}/{}  train_loss: {:.4f}, train_acc: {:.4f}, val_loss: {:.4f}, val_acc: {:.4f}'.format(
				epoch + 1, self.max_iter, losses / total, correct / total, val_loss, val_acc
			))
			if epoch > 5 and val_acc > best_acc:
				best_acc = val_acc
				best_model = self.model

			if val_acc >= best_acc:  # val_acc提升
				cnt = 0

			if last_acc == val_acc:  # val_acc不在变化
				cnt2 += 1
			else:
				cnt2 = 0

			last_acc = val_acc
			cnt += 1
			if epoch > 5 and (
					cnt > self.early_stopping_rounds or cnt2 > self.early_stopping_rounds):  # x次epoch的val_acc不提升或x次epoch的val_acc不变化
				print("Early stopping at epoch-{}/{}".format(epoch + 1, self.max_iter))
				break

		return best_model

	def eval(self):
		total = 0.0
		losses = 0.0
		correct = 0.0
		self.model.eval()
		with torch.no_grad():
			for x, y in self.eval_loader:
				x, y = x.to(self.device), y.to(self.device)
				loss, logits = self.model(x, y)
				correct += (logits.argmax(1) == y).sum().item()
				losses += loss.item()
				total += len(y)
		return losses / total, correct / total


class SimpleTrainer(Trainer):

	def __init__(self, model, X, y, eval_size=0.2, random_state=None, collate_fn=None,
				 max_iter=100, optimizer=optim.AdamW, learning_rate=0.001,
				 batch_size=8, eval_batch_size=16,
				 num_workers=4, num_eval_workers=2,
				 early_stopping_rounds=10,  # 早停，等10轮决策，评价指标不在变化，停止
				 device=torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')):
		X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=eval_size, random_state=random_state)
		super().__init__(model,
						 TensorDataset(X_train, y_train),
						 TensorDataset(X_test, y_test),
						 collate_fn,
						 max_iter,
						 optimizer,
						 learning_rate,
						 batch_size,
						 eval_batch_size,
						 num_workers,
						 num_eval_workers,
						 early_stopping_rounds,
						 device
						 )
