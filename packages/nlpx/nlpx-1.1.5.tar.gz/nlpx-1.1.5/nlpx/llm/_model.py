import torch
from torch import optim
from pathlib import Path
from typing import Union, List
from nlpx.training import SimpleTrainer, evaluate
from torch.utils.data import DataLoader, TensorDataset
from nlpx.text_token import get_texts_max_length


class Model:

	def __init__(self, tokenize_vec, model_path: Union[str, Path] = None, classes: List[str] = None,
					device=torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')):
		self.tokenize_vec = tokenize_vec
		self.classes = classes
		self.model = torch.load(model_path, map_location=device) if model_path else None
		self.device = device

	def train(self, model, texts: List[str], y: torch.Tensor, max_length: int = None,
			  eval_size=0.2, random_state=None, collate_fn=None,max_iter=100,
			  optimizer=optim.AdamW, learning_rate=0.001, T_max: int = 0,
			  batch_size=8, eval_batch_size=16,
			  num_workers=4, num_eval_workers=2,
			  early_stopping_rounds=10):
		max_length = max_length or self.get_max_length(texts)
		X = self._get_vec(texts, max_length=max_length)
		trainer = SimpleTrainer(model, X, y, eval_size, random_state, collate_fn,
								 max_iter, optimizer, learning_rate, T_max,
								 batch_size, eval_batch_size,
								 num_workers, num_eval_workers,
								 early_stopping_rounds,  # 早停，等10轮决策，评价指标不在变化，停止
								 self.device)
		self.model = trainer.train()

	def predict(self, texts: List[str]):
		max_length = self.get_max_length(texts)
		X = self._get_vec(texts, max_length=max_length)
		self.model.eval()
		with torch.no_grad():
			logits = self.model(X)
		return logits.argmax(1)

	def predict_classes(self, texts: List[str]):
		assert self.classes is not None, 'classes must be specified'
		pred = self.predict(texts)
		return [self.classes[i] for i in pred.detach().numpy().ravel()]

	def evaluate(self, texts: List[str], y: torch.LongTensor, batch_size=16, num_workers=0, collate_fn=None):
		max_length = self.get_max_length(texts)
		X = self._get_vec(texts, max_length=max_length)
		eval_set = TensorDataset(X, y)
		eval_loader = DataLoader(dataset=eval_set, batch_size=batch_size,
								 num_workers=num_workers, collate_fn=collate_fn)
		return evaluate(self.model, eval_loader, self.device)

	def _get_vec(self, texts: List[str], max_length: int):
		return self.tokenize_vec.parallel_encode_plus(texts, max_length=max_length, padding='max_length',
														truncation=True, add_special_tokens=True,
														return_token_type_ids=True,return_attention_mask=True,
														return_tensors='pt')

	@staticmethod
	def get_max_length(texts: List[str]) -> int:
		return get_texts_max_length(texts, cut_type='char')


# class SimpleModel:
#
# 	def __init__(self, tokenize_vec, model_path: Union[str, Path], classes: List[str] = None,
# 					device=torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')):
# 		self.tokenize_vec = tokenize_vec
# 		self.classes = classes
# 		self.model = torch.load(model_path, map_location=device) if model_path else None
#
# 	def train(self, train_set: Dataset, eval_set: Dataset, collate_fn=None,max_iter=100,
# 				optimizer=optim.AdamW, learning_rate=0.001, T_max: int = 0,
# 				batch_size=8, eval_batch_size=16,
# 				num_workers=4, num_eval_workers=2,
# 				early_stopping_rounds=10):

