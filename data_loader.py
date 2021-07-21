import json
import logging
import os

logger = logging.getLogger(__name__)


class YnatProcessor(object): # object는 python 3에선 그냥 취향껏 선택 (구현에 영향 X)
    """Processor for the YNAT data set"""

    def __init__(self, args):
        self.args = args

    @classmethod # this method is passed the actual class object as an argument
    def _read_file(cls, input_file, quotechar=None):
        """Reads a json value file, return array of dict objects"""
        with open(input_file, 'r') as data_file:
            json_data = data_file.read()
        data = json.loads(json_data) # list of json objects
        data_file.close()
        return data

    def _create_examples(self, data, set_type):
        print('enter create_examples')

    def get_examples(self, mode):
        """
        Args:
            mode: train, dev, test
        """
        file_to_read = None
        if mode == 'train':
            file_to_read = self.args.train_file
        elif mode == 'dev': # dev는 뭐지???
            file_to_read = self.args.dev_file
        elif mode == 'test':
            file_to_read = self.args.test_file

        logger.info("LOOKING AT {}".format(os.path.join(self.args.data_dir, file_to_read)))
        return self._create_examples(self._read_file(os.path.join(self.args.data_dir, file_to_read)), mode)


processors = {
    "ynat": YnatProcessor,
}


def load_and_cache_examples(args, tokenizer, mode):
    processor = processors[args.task](args)

    logger.info("Creating features from dataset file at %s", args.data_dir)
    examples = processor.get_examples("train")

    return examples