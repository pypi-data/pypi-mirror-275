import torch
from pathlib import Path
from joblib import Parallel, delayed
from typing import Union, List, Optional
from transformers import BertTokenizer, BertConfig, BertModel, AutoModel
from transformers.tokenization_utils import PaddingStrategy, TruncationStrategy, TensorType


class TokenizeVec:

	def __init__(self, pretrained_path: Union[str, Path]):
		self.pretrained = None
		self.tokenizer = BertTokenizer.from_pretrained(pretrained_path)

	def encode_plus(self,
				texts: List[str],
				add_special_tokens: bool = True,
				padding: Union[bool, str, PaddingStrategy] = False,
				truncation: Union[bool, str, TruncationStrategy] = None,
				max_length: Optional[int] = None,
				stride: int = 0,
				is_split_into_words: bool = False,
				pad_to_multiple_of: Optional[int] = None,
				return_tensors: Optional[Union[str, TensorType]] = None,
				return_token_type_ids: Optional[bool] = None,
				return_attention_mask: Optional[bool] = None,
				return_overflowing_tokens: bool = False,
				return_special_tokens_mask: bool = False,
				return_offsets_mapping: bool = False,
				return_length: bool = False,
				verbose: bool = True,
				cls: bool = False,
				**kwargs,
			) -> torch.FloatTensor:
		tokens = self.tokenizer.batch_encode_plus(
												texts,
												add_special_tokens,
												padding,
												truncation,
												max_length,
												stride,
												is_split_into_words,
												pad_to_multiple_of,
												return_tensors,
												return_token_type_ids,
												return_attention_mask,
												return_overflowing_tokens,
												return_special_tokens_mask,
												return_offsets_mapping,
												return_length,
												verbose,
												** kwargs
											)
		self.pretrained.eval()
		with torch.no_grad():
			output = self.pretrained(**tokens, output_hidden_states=True)
		return output.last_hidden_state[:, 0] if cls else output.last_hidden_state[:, 1:]

	def batch_encode_plus(self,
						texts: List[str],
						add_special_tokens: bool = True,
						padding: Union[bool, str, PaddingStrategy] = False,
						truncation: Union[bool, str, TruncationStrategy] = None,
						max_length: Optional[int] = None,
						stride: int = 0,
						is_split_into_words: bool = False,
						pad_to_multiple_of: Optional[int] = None,
						return_tensors: Optional[Union[str, TensorType]] = None,
						return_token_type_ids: Optional[bool] = None,
						return_attention_mask: Optional[bool] = None,
						return_overflowing_tokens: bool = False,
						return_special_tokens_mask: bool = False,
						return_offsets_mapping: bool = False,
						return_length: bool = False,
						verbose: bool = True,
						cls: bool = False,
						batch_size: int = 128,
						**kwargs,
					) -> torch.FloatTensor:
		length = len(texts)
		if length <= batch_size:
			return self.encode_plus(
									texts,
									add_special_tokens,
									padding,
									truncation,
									max_length,
									stride,
									is_split_into_words,
									pad_to_multiple_of,
									return_tensors,
									return_token_type_ids,
									return_attention_mask,
									return_overflowing_tokens,
									return_special_tokens_mask,
									return_offsets_mapping,
									return_length,
									verbose,
									cls,
									** kwargs
								)
		else:
			text_list = self.split_texts(texts, batch_size)
			results = [self.encode_plus(
									text,
									add_special_tokens,
									padding,
									truncation,
									max_length,
									stride,
									is_split_into_words,
									pad_to_multiple_of,
									return_tensors,
									return_token_type_ids,
									return_attention_mask,
									return_overflowing_tokens,
									return_special_tokens_mask,
									return_offsets_mapping,
									return_length,
									verbose,
									cls,
									** kwargs
								) for text in text_list]
			return torch.concat(results, dim=0)

	def parallel_encode_plus(self,
						texts: List[str],
						add_special_tokens: bool = True,
						padding: Union[bool, str, PaddingStrategy] = False,
						truncation: Union[bool, str, TruncationStrategy] = None,
						max_length: Optional[int] = None,
						stride: int = 0,
						is_split_into_words: bool = False,
						pad_to_multiple_of: Optional[int] = None,
						return_tensors: Optional[Union[str, TensorType]] = None,
						return_token_type_ids: Optional[bool] = None,
						return_attention_mask: Optional[bool] = None,
						return_overflowing_tokens: bool = False,
						return_special_tokens_mask: bool = False,
						return_offsets_mapping: bool = False,
						return_length: bool = False,
						verbose: bool = True,
						cls: bool = False,
						batch_size: int = 128,
						n_jobs: int = -1,
						**kwargs,
					) -> torch.FloatTensor:
		length = len(texts)
		if length <= batch_size:
			return self.encode_plus(
									texts,
									add_special_tokens,
									padding,
									truncation,
									max_length,
									stride,
									is_split_into_words,
									pad_to_multiple_of,
									return_tensors,
									return_token_type_ids,
									return_attention_mask,
									return_overflowing_tokens,
									return_special_tokens_mask,
									return_offsets_mapping,
									return_length,
									verbose,
									cls,
									** kwargs
								)
		else:
			text_list = self.split_texts(texts, batch_size)
			results = Parallel(n_jobs=n_jobs)(
				delayed(self._order_encode)(i,
											text,
											add_special_tokens,
											padding,
											truncation,
											max_length,
											stride,
											is_split_into_words,
											pad_to_multiple_of,
											return_tensors,
											return_token_type_ids,
											return_attention_mask,
											return_overflowing_tokens,
											return_special_tokens_mask,
											return_offsets_mapping,
											return_length,
											verbose,
											cls,
											**kwargs
										) for i, text in enumerate(text_list))
			results = sorted(results, key=lambda x: x[0], reverse=False)
			results = [r[1] for r in results]
			return torch.concat(results, dim=0)

	@staticmethod
	def split_texts(texts: List[str], batch_size: int):
		return [texts[i:i + batch_size] for i in range(0, len(texts), batch_size)]

	def _order_encode(self,
				order: int,
				texts: List[str],
				add_special_tokens: bool = True,
				padding: Union[bool, str, PaddingStrategy] = False,
				truncation: Union[bool, str, TruncationStrategy] = None,
				max_length: Optional[int] = None,
				stride: int = 0,
				is_split_into_words: bool = False,
				pad_to_multiple_of: Optional[int] = None,
				return_tensors: Optional[Union[str, TensorType]] = None,
				return_token_type_ids: Optional[bool] = None,
				return_attention_mask: Optional[bool] = None,
				return_overflowing_tokens: bool = False,
				return_special_tokens_mask: bool = False,
				return_offsets_mapping: bool = False,
				return_length: bool = False,
				verbose: bool = True,
				cls: bool = False,
				**kwargs,
			) -> torch.FloatTensor:
		return order, self.encode_plus(
								texts,
								add_special_tokens,
								padding,
								truncation,
								max_length,
								stride,
								is_split_into_words,
								pad_to_multiple_of,
								return_tensors,
								return_token_type_ids,
								return_attention_mask,
								return_overflowing_tokens,
								return_special_tokens_mask,
								return_offsets_mapping,
								return_length,
								verbose,
								cls,
								**kwargs
							)


class BertTokenizeVec(TokenizeVec):

	def __init__(self, pretrained_path: Union[str, Path]):
		super().__init__(pretrained_path)
		bert_config = BertConfig.from_pretrained(pretrained_path)
		self.pretrained = BertModel.from_pretrained(pretrained_path, config=bert_config)


class ErnieTokenizeVec(TokenizeVec):

	def __init__(self, pretrained_path: Union[str, Path]):
		super().__init__(pretrained_path)
		self.pretrained = AutoModel.from_pretrained(pretrained_path)
