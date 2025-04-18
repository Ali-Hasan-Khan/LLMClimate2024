# coding=utf-8
# Copyright 2020 The HuggingFace Datasets Authors and the current dataset script contributor.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Sum-IPCC: Climate Change Report Summarization with Large Language Models"""

import os
import datasets
import yaml
import textwrap


_CITATION = """
@misc{IPCC,
      title={Climate Change Report Summarization with Large Language Models}, 
      author={Leonardo Catalano, Tommaso Colella and Iacopo Ghinassi},
      year={2024},
      eprint={},
      archivePrefix={},
      primaryClass={}
}
"""

_DESCRIPTION = """\
A dataset for summarization for policy makers of IPCC synthesis reports for climate change.
"""

_HOMEPAGE = ""

_LICENSE = ""

_SumIPCCsum_BASE_KWARGS = dict(
    citation=_CITATION,
    url=_HOMEPAGE,
)


class SumIPCCConfig(datasets.BuilderConfig):
    """BuilderConfig for Climabench."""

    def __init__(
        self,
        data_dir,
        citation,
        url,
        **kwargs,
    ):
        """BuilderConfig for Climabench.
        Args:
          data_dir: `string`, the path to the folder containing the tsv files in the
            downloaded zip
        """
        super(SumIPCCConfig, self).__init__(
            version=datasets.Version("1.0.0", ""), **kwargs
        )
        self.data_dir = data_dir
        self.citation = citation
        self.url = url


class SumIPCC(datasets.GeneratorBasedBuilder):
    """SumIPCC dataset."""

    BUILDER_CONFIGS = [
        SumIPCCConfig(
            name="AR6",
            description=textwrap.dedent(
            """
            This Synthesis Report (SYR) of the IPCC Sixth Assessment Report (AR6)
            summarises the state of knowledge of climate change, its widespread
            impacts and risks, and climate change mitigation and adaptation, based
            on the peer-reviewed scientific, technical and socio-economic literature
            since the publication of the IPCC’s Fifth Assessment Report (AR5) in
            2014.
            The assessment is undertaken within the context of the evolving
            international landscape, in particular, developments in the UN
            Framework Convention on Climate Change (UNFCCC) process,
            including the outcomes of the Kyoto Protocol and the adoption of the
            Paris Agreement. It reflects the increasing diversity of those involved in
            climate action.
            This report integrates the main findings of the AR6 Working Group
            reports58 and the three AR6 Special Reports 59
            . It recognizes the
            interdependence of climate, ecosystems and biodiversity, and human
            societies; the value of diverse forms of knowledge; and the close
            linkages between climate change adaptation, mitigation, ecosystem
            health, human well-being and sustainable development. Building on
            multiple analytical frameworks, including those from the physical and
            social sciences, this report identifies opportunities for transformative
            action which are effective, feasible, just and equitable using concepts
            of systems transitions and resilient development pathways 60
            . Different
            regional classification schemes 61 are used for physical, social and
            economic aspects, reflecting the underlying literature.
            After this introduction, Section 2, ‘Current Status and Trends’, opens
            with the assessment of observational evidence for our changing
            climate, historical and current drivers of human-induced climate
            change, and its impacts. It assesses the current implementation of
            adaptation and mitigation response options. Section 3, ‘Long-Term
            Climate and Development Futures’, provides a long-term assessment of
            climate change to 2100 and beyond in a broad range of socio-economic
            futures. It considers long-term characteristics, impacts, risks and costs
            in adaptation and mitigation pathways in the context of sustainable
            development. Section 4, ‘Near- Term Responses in a Changing Climate’,
            assesses opportunities for scaling up effective action in the period up
            to 2040, in the context of climate pledges, and commitments, and the
            pursuit of sustainable development.
            Based on scientific understanding, key findings can be formulated as
            statements of fact or associated with an assessed level of confidence
            using the IPCC calibrated language62
            . The scientific findings are
            drawn from the underlying reports and arise from their Summary for
            Policymakers (hereafter SPM), Technical Summary (hereafter TS), and
            underlying chapters and are indicated by {} brackets. Figure 1.1 shows
            the Synthesis Report Figures Key, a guide to visual icons that are used
            across multiple figures within this report.
            """
            ),
            data_dir="all_data/AR6",
            citation=textwrap.dedent(
                """\
             @misc{IPCCAR6,
                    title = {AR6 Synthesis Report Climate Change 2023},
                    author = {IPCC},
                    year={2024}
                    url = {https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_LongerReport.pdf},
                }
            }"""
            ),
            url="https://www.ipcc.ch/report/ar6/syr/",
        ),
        SumIPCCConfig(
            name="AR5",
            description=textwrap.dedent(
            """
    	    The Synthesis Report (SYR), constituting the final product of the Fifth
	    Assessment Report (AR5) of the Intergovernmental Panel on Climate
	    Change (IPCC), is published under the title Climate Change 2014. This
	    report distils, synthesizes and integrates the key findings of the three
	    Working Group contributions – The Physical Science Basis, Impacts,
	    Adaptation, and Vulnerability and Mitigation of Climate Change – to
	    the AR5 in a concise document for the benefit of decision makers in
	    the government, the private sector as well as the public at large. The
	    SYR also draws on the findings of the two Special Reports brought out
	    in 2011 dealing with Renewable Energy Sources and Climate Change
	    Mitigation, and Managing the Risks of Extreme Events and Disasters to
	    Advance Climate Change Adaptation. The SYR, therefore, is a compre-
	    hensive up-to-date compilation of assessments dealing with climate
	    change, based on the most recent scientific, technical and socio-economic
	    literature in the field.
            """
            ),
            data_dir="all_data/AR5",
            citation=textwrap.dedent(
                """\
             @misc{IPCCAR5,
                    title = {AR5 Synthesis Report: Climate Change 2014},
                    author = {IPCC},
                    year={2014}
                    url = {https://www.ipcc.ch/site/assets/uploads/2018/02/SYR_AR5_FINAL_full.pdf},
                }
            }"""
            ),
            url="https://www.ipcc.ch/report/ar5/syr/",
        ),
        SumIPCCConfig(
            name="ALL",
            description=textwrap.dedent(
            """
            The concatenation of AR5 and AR6 synthesis reports from IPCC
            """
            ),
            data_dir="all_data",
            citation=textwrap.dedent(
                """\
             @misc{IPCC,
                    title = {IPCC Homepage},
                    author = {IPCC},
                    year={2024}
                    url = {https://www.ipcc.ch/},
                }
            }"""
            ),
            url="https://www.ipcc.ch/"
        )
        ]
    
    def _info(self):
        features = datasets.Features(
                    {
                        "full_paragraphs": datasets.Sequence(datasets.Value("string")),
                        "summary": datasets.Value("string"),
                        "summary_topic": datasets.Value("string"),
                        "paragraph_topic": datasets.Value("string"),
                        "section_topic": datasets.Value("string"),
                        "source": datasets.Value("string"),
                        "paragraph_ids": datasets.Sequence(datasets.Value("string")),
                        "paragraph_titles": datasets.Sequence(datasets.Value("string")),
                        "ID": datasets.Value("string")
                    }
        )

        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=datasets.Features(features),
            homepage=self.config.url,
            citation=self.config.citation + "\n" + _CITATION,
        )
    
    def _split_generators(self, dl_manager):
        data_dir = self.config.data_dir

        if self.config.name == "ALL":
            files = []
            for root, directs, _ in os.walk(data_dir):
                for direct in directs:
                    file_name = [file for file in os.listdir(os.path.join(root, direct)) if file.endswith("yaml")]
                    assert len(file_name) == 1, "Too many yaml files in directory"
                    file_name = file_name[0]
                    files.append(os.path.join(root, direct, file_name))
        else:
            files = []
            for root, _, fls in os.walk(data_dir):
                file_name = [file for file in fls if file.endswith("yaml")]
                assert len(file_name) == 1, "Too many yaml files in directory"
                file_name = file_name[0]
                files.append(os.path.join(root, file_name))

        return [
                datasets.SplitGenerator(
                    name=datasets.Split.TEST,
                    gen_kwargs={
                        "data_files": files,
                        "split": "test",
                    },
                ),
            ]

    def _generate_examples(self, data_files, split):
        #idx = iter(range(10000))
        idx = -1
        for data_file in data_files:
            with open(data_file, encoding='utf-8') as f:
                doc = yaml.safe_load(f)
                for identifier in doc["summaries"]:
                    idx += 1
                    yield from self._process_example(doc, identifier, data_file, idx)

    def _process_example(self, doc, 
                         identifier, 
                         source,
                         idx):
        
        summary = doc["summaries"][identifier]
        full_para = doc["full_paragraphs"][identifier]
        
        para_topic = doc["paragraph_topics"][identifier]
        sect_topic = doc["section_topics"][identifier]
        summary_topic = doc["summary_topics"][identifier]
        
        para_id = doc["pointers"][identifier]
        para_title = doc["titles"][identifier]

        yield idx, {"full_paragraphs": full_para,
                "summary": summary,
                "paragraph_topic": para_topic,
                "section_topic": sect_topic,
                "summary_topic": summary_topic,
                "source": source,
                "paragraph_ids": para_id,
                "paragraph_titles": para_title,
                "ID": identifier}

    # do this in some postprocess function after generating yaml    
    # def _clean(self, text):
    #     text = re.sub("\n", " ", text)
    #     text = re.sub("'", "", text)
    #     return text.strip()
