from unittest import TestCase
from getdeck.deckfile.file import DeckfileInlineSource
from getdeck.fetch.types import DeckfileAux, SourceAux
from getdeck.sources.inline import Inline
import itertools


class InlineTest(TestCase):
    def test_render(self):
        test_namespaces = [None, "default", "test"]
        test_contents = [{}]
        combinations = itertools.product(test_namespaces, test_contents)

        for combination in combinations:
            namespace = combination[0]
            content = combination[1]

            deckfile_aux = DeckfileAux(location="test")
            source_aux = SourceAux(source=DeckfileInlineSource(content=content))

            render_behavior = Inline(
                path=None,
                source=None,
                config=None,
                namespace=namespace,
            )
            source_files = render_behavior.render(
                deckfile_aux=deckfile_aux, source_aux=source_aux
            )

            self.assertEqual(len(source_files), 1)
            source_file = source_files[0]
            self.assertEqual(source_file.namespace, namespace or "default")
            self.assertEqual(source_file.content, content)
