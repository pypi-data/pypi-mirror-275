#!/usr/bin/env python3

"""Module containing the Curves class and the command line interface."""
import os
import zipfile
import argparse
import shutil
from pathlib import Path
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.configuration import settings
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger


class Curves(BiobbObject):
    """
    | biobb_dna Curves
    | Wrapper for the Cur+ executable  that is part of the Curves+ software suite.
    | The Cur+ program is used to analyze the structure of nucleic acids and their complexes.

    Args:
        input_struc_path (str): Trajectory or PDB input file. File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_dna/master/biobb_dna/test/data/curvesplus/structure.stripped.trj>`_. Accepted formats: trj (edam:format_3910), pdb (edam:format_1476), netcdf (edam:format_3650), nc (edam:format_3650).
        input_top_path (str) (Optional): Topology file, needed along with .trj file (optional). File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_dna/master/biobb_dna/test/data/curvesplus/structure.stripped.top>`_. Accepted formats: top (edam:format_3881).
        output_cda_path (str): Filename for Curves+ output .cda file. File type: output. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_dna/master/biobb_dna/test/reference/curvesplus/curves_trj_output.cda>`_. Accepted formats: cda (edam:format_2330).
        output_lis_path (str): Filename for Curves+ output .lis file. File type: output. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_dna/master/biobb_dna/test/reference/curvesplus/curves_trj_output.lis>`_. Accepted formats: lis (edam:format_2330).
        output_zip_path (str) (Optional): Filename for .zip files containing Curves+ output that is not .cda or .lis files. File type: output. Accepted formats: zip (edam:format_3987).
        properties (dict):
            * **s1range** (*str*) - (None) Range of first strand. Must be specified in the form "start:end".
            * **s2range** (*str*) - (None) Range of second strand. Must be specified in the form "start:end".
            * **stdlib_path** (*str*) - ('standard') Path to Curves' standard library files for nucleotides. If not specified will look for 'standard' files in current directory.
            * **itst** (*int*) - (0) Iteration start index.
            * **itnd** (*int*) - (0) Iteration end index.
            * **itdel** (*int*) - (1) Iteration delimiter.
            * **ions** (*bool*) - (False) If True, helicoidal analysis of ions (or solvent molecules) around solute is carried out.
            * **test** (*bool*) - (False) If True, provide addition output in .lis file on fitting and axis generation.
            * **line** (*bool*) - (False) if True, find the best linear helical axis.
            * **fit** (*bool*) - (True) if True, fit a standard bases to the input coordinates (important for MD snapshots to avoid base distortions leading to noisy helical parameters).
            * **axfrm** (*bool*) - (False) if True, generates closely spaced helical axis frames as input for Canal and Canion.
            * **binary_path** (*str*) - (Cur+) Path to Curves+ executable, otherwise the program wil look for Cur+ executable in the binaries folder.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_dna.curvesplus.biobb_curves import biobb_curves
            prop = {
                's1range': '1:12',
                's2range': '24:13',
            }
            biobb_curves(
                input_struc_path='/path/to/structure/file.trj',
                input_top_path='/path/to/topology/file.top',
                output_cda_path='/path/to/output/file.cda',
                output_lis_path='/path/to/output/file.lis',
                properties=prop)
    Info:
        * wrapped_software:
            * name: Curves
            * version: >=2.6
            * license: BSD 3-Clause
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl
    """

    def __init__(
            self, input_struc_path, output_lis_path,
            output_cda_path, output_zip_path=None,
            input_top_path=None, properties=None, **kwargs) -> None:
        properties = properties or {}

        # Call parent class constructor
        super().__init__(properties)
        self.locals_var_dict = locals().copy()

        # Input/Output files
        self.io_dict = {
            'in': {
                'input_struc_path': input_struc_path,
                'input_top_path': input_top_path
            },
            'out': {
                'output_lis_path': output_lis_path,
                'output_cda_path': output_cda_path,
                'output_zip_path': output_zip_path
            }
        }

        # Properties specific for BB
        self.s1range = properties.get('s1range', None)
        self.binary_path = properties.get('binary_path', 'Cur+')
        self.stdlib_path = properties.get('stdlib_path', None)
        self.s2range = properties.get('s2range', None)
        self.itst = properties.get('itst', 0)
        self.itnd = properties.get('itnd', 0)
        self.itdel = properties.get('itdel', 1)
        self.ions = properties.get('ions', '.f.')
        self.test = properties.get('test', '.f.')
        self.line = properties.get('line', '.f.')
        self.fit = properties.get('fit', '.t.')
        self.axfrm = properties.get('axfrm', '.f.')
        self.properties = properties

        # Check the properties
        self.check_properties(properties)
        self.check_arguments()

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`Curves <biobb_dna.curvesplus.biobb_curves.Curves>` object."""

        # Setup Biobb
        if self.check_restart():
            return 0
        self.stage_files()

        if self.s1range is None:
            raise ValueError("property 's1range' must be specified!")
        if self.s2range is None:
            # compute s2range if not provided
            range1_end = int(self.s1range.split(":")[1])
            s2start = range1_end + 1
            s2end = 2 * range1_end
            self.s2range = f"{s2end}:{s2start}"

        # check standard library files location if not provided
        if self.stdlib_path is None:
            if os.getenv("CONDA_PREFIX", False):
                curves_aux_path = Path(
                    os.getenv("CONDA_PREFIX")) / ".curvesplus"
                # check if .curvesplus directory is in $CONDA_PREFIX
                if curves_aux_path.exists():
                    if len(list(curves_aux_path.glob("standard_*.lib"))) != 3:
                        raise FileNotFoundError(
                            "One or all standard library files "
                            f"missing from {curves_aux_path}! "
                            "Check files standard_b.lib, "
                            "standard_s.lib and standard_i.lib exist.")
                    self.stdlib_path = curves_aux_path / "standard"
                else:
                    raise FileNotFoundError(
                        ".curvesplus directory not found in "
                        f"{os.getenv('CONDA_PREFIX')} !"
                        "Please indicate where standard_*.lib files are "
                        "located with the stdlib_path property.")
            else:
                # CONDA_PREFIX undefined
                self.stdlib_path = Path.cwd() / "standard"

        # Creating temporary folder
        self.tmp_folder = fu.create_unique_dir(prefix="curves_")
        fu.log('Creating %s temporary folder' % self.tmp_folder, self.out_log)

        # copy input files to temporary folder
        shutil.copy(self.io_dict['in']['input_struc_path'], self.tmp_folder)
        tmp_struc_input = Path(self.io_dict['in']['input_struc_path']).name
        if self.io_dict['in']['input_top_path'] is not None:
            shutil.copy(self.io_dict['in']['input_top_path'], self.tmp_folder)
            tmp_top_input = Path(self.io_dict['in']['input_top_path']).name

        # change directory to temporary folder
        original_directory = os.getcwd()
        os.chdir(self.tmp_folder)

        # create intructions
        instructions = [
            f"{self.binary_path} <<! ",
            "&inp",
            f"  file={tmp_struc_input},"]
        if self.io_dict['in']['input_top_path'] is not None:
            # add topology file if needed
            fu.log('Appending provided topology to command',
                   self.out_log, self.global_log)
            instructions.append(
                f"  ftop={tmp_top_input},")

        # create intructions
        instructions = instructions + [
            "  lis='curves_output',",
            f"  lib={self.stdlib_path},",
            f"  ions={self.ions},",
            f"  test={self.test},",
            f"  line={self.line},",
            f"  fit={self.fit},",
            f"  axfrm={self.axfrm},",
            f"  itst={self.itst},itnd={self.itnd},itdel={self.itdel},",
            "&end",
            "2 1 -1 0 0",
            f"{self.s1range}",
            f"{self.s2range}",
            "!"
        ]
        self.cmd = ["\n".join(instructions)]
        fu.log('Creating command line with instructions and required arguments',
               self.out_log, self.global_log)

        # Run Biobb block
        self.run_biobb()

        # change back to original directory
        os.chdir(original_directory)

        # create zipfile and write output inside
        if self.io_dict["out"]["output_zip_path"] is not None:
            zf = zipfile.ZipFile(
                Path(self.io_dict["out"]["output_zip_path"]),
                "w")
            for curves_outfile in Path(self.tmp_folder).glob("curves_output*"):
                if curves_outfile.suffix not in (".cda", ".lis"):
                    zf.write(
                        curves_outfile,
                        arcname=curves_outfile.name)
            zf.close()

        # rename cda and lis files
        (Path(self.tmp_folder) / "curves_output.cda").rename(
            self.io_dict["out"]["output_cda_path"])
        (Path(self.tmp_folder) / "curves_output.lis").rename(
            self.io_dict["out"]["output_lis_path"])

        # Remove temporary file(s)
        self.tmp_files.extend([
            self.stage_io_dict.get("unique_dir"),
            self.tmp_folder
        ])
        self.remove_tmp_files()

        self.check_arguments(output_files_created=True, raise_exception=False)

        return self.return_code


def biobb_curves(
        input_struc_path: str, output_lis_path: str, output_cda_path: str,
        input_top_path: str = None, output_zip_path: str = None,
        properties: dict = None, **kwargs) -> int:
    """Create :class:`Curves <biobb_dna.curvesplus.biobb_curves.Curves>` class and
    execute the :meth:`launch() <biobb_dna.curvesplus.biobb_curves.Curves.launch>` method."""

    return Curves(
        input_struc_path=input_struc_path,
        input_top_path=input_top_path,
        output_lis_path=output_lis_path,
        output_cda_path=output_cda_path,
        output_zip_path=output_zip_path,
        properties=properties, **kwargs).launch()


def main():
    """Command line execution of this building block. Please check the command line documentation."""
    parser = argparse.ArgumentParser(description='Execute Cur+ form the Curves+ software suite.',
                                     formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('--config', required=False, help='Configuration file')

    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('--input_struc_path', required=True,
                               help='Trajectory or PDB input file. Accepted formats: trj, pdb.')
    required_args.add_argument('--output_cda_path', required=True,
                               help='Filename to give to output .cda file. Accepted formats: str.')
    required_args.add_argument('--output_lis_path', required=True,
                               help='Filename to give to output .lis file. Accepted formats: str.')
    parser.add_argument('--input_top_path', required=False,
                        help='Topology file, needed along with .trj file (optional). Accepted formats: top.')
    parser.add_argument('--output_zip_path', required=False,
                        help='Filename to give to output files (except .cda and .lis files). Accepted formats: str.')

    args = parser.parse_args()
    args.config = args.config or "{}"
    properties = settings.ConfReader(config=args.config).get_prop_dic()

    biobb_curves(
        input_struc_path=args.input_struc_path,
        input_top_path=args.input_top_path,
        output_cda_path=args.output_cda_path,
        output_lis_path=args.output_lis_path,
        output_zip_path=args.output_zip_path,
        properties=properties)


if __name__ == '__main__':
    main()
